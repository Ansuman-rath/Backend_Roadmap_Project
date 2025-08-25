const express = require('express');
const router = express.Router();
const multer = require('multer');
const upload = multer();
const auth = require('../middlewares/authMiddleware');
const { transformLimiter } = require('../middlewares/rateLimit');
const { uploadImage, transformImage, getImage, listImages } = require('../controllers/imageController');

router.post('/images', auth, upload.single('image'), uploadImage);
router.post('/images/:id/transform', auth, transformLimiter, transformImage);
router.get('/images/:id', auth, getImage);
router.get('/images', auth, listImages);

module.exports = router;
