const Order = require('../models/Order');
const Cart = require('../models/Cart');
const Product = require('../models/Product');

// Checkout / create order
exports.createOrder = async (req, res) => {
    try {
        const cart = await Cart.findOne({ userId: req.user.id });
        if (!cart || cart.products.length === 0) return res.status(400).json({ message: 'Cart is empty' });

        let totalAmount = 0;
        for (const item of cart.products) {
            const product = await Product.findById(item.productId);
            if (!product) continue;
            totalAmount += product.price * item.quantity;
        }

        const order = await Order.create({
            userId: req.user.id,
            products: cart.products,
            totalAmount,
            status: 'Paid', // Simulate payment
        });

        cart.products = [];
        await cart.save();

        res.status(201).json(order);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};

// Get all orders for user
exports.getOrders = async (req, res) => {
    try {
        const orders = await Order.find({ userId: req.user.id });
        res.json(orders);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};
