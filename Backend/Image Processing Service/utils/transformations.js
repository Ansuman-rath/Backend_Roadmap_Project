const sharp = require('sharp');
const axios = require('axios');

const applyTransformations = async (url, transformations) => {
  const response = await axios({ url, responseType: 'arraybuffer' });
  let image = sharp(response.data);

  if (transformations.resize) {
    image = image.resize(transformations.resize.width, transformations.resize.height);
  }
  if (transformations.rotate) {
    image = image.rotate(transformations.rotate);
  }
  if (transformations.flip) image = image.flip();
  if (transformations.flop) image = image.flop();
  if (transformations.format) image = image.toFormat(transformations.format);
  if (transformations.filters) {
    if (transformations.filters.grayscale) image = image.grayscale();
    if (transformations.filters.sepia) image = image.modulate({ saturation: 0.5, hue: 30 });
  }

  const buffer = await image.toBuffer();
  return buffer; // Can upload transformed buffer to S3
};

module.exports = { applyTransformations };
