const express = require('express');
const router = express.Router();
const { auth } = require('../middleware/authMiddleware');
const { createOrder, getOrders } = require('../controllers/orderController');

router.post('/checkout', auth, createOrder);
router.get('/', auth, getOrders);

module.exports = router;
