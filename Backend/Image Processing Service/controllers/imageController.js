const Image = require('../models/Image');
const { uploadToS3 } = require('../utils/s3');
const { applyTransformations } = require('../utils/transformations');

exports.uploadImage = async (req, res) => {
  const file = req.file;
  if (!file) return res.status(400).json({ message: 'No file uploaded' });

  const url = await uploadToS3(file);
  const image = await Image.create({
    user: req.user._id,
    url,
    metadata: { size: file.size, type: file.mimetype }
  });
  res.status(201).json(image);
};

exports.transformImage = async (req, res) => {
  const { id } = req.params;
  const { transformations } = req.body;
  const image = await Image.findById(id);
  if (!image) return res.status(404).json({ message: 'Image not found' });

  const buffer = await applyTransformations(image.url, transformations);
  const transformedFile = { originalname: 'transformed.png', buffer, mimetype: 'image/png' };
  const transformedUrl = await uploadToS3(transformedFile);

  image.transformations.push(transformations);
  await image.save();

  res.json({ ...image.toObject(), transformedUrl });
};

exports.getImage = async (req, res) => {
  const image = await Image.findById(req.params.id);
  if (!image) return res.status(404).json({ message: 'Image not found' });
  res.json(image);
};

exports.listImages = async (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const images = await Image.find({ user: req.user._id })
    .skip((page - 1) * limit)
    .limit(limit)
    .sort({ createdAt: -1 });
  res.json(images);
};
