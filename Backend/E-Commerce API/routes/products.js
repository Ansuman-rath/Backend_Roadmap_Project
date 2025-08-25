const express = require('express');
const router = express.Router();

const { 
    createProduct, 
    getProducts, 
    getProductById, 
    updateProduct, 
    deleteProduct 
} = require('../controllers/productController');
const { auth, admin } = require('../middleware/authMiddleware');

router.post('/', auth, admin, createProduct);
router.get('/', getProducts);
router.get('/:id', getProductById);
router.put('/:id', auth, admin, updateProduct);   
router.delete('/:id', auth, admin, deleteProduct); 

module.exports = router;



