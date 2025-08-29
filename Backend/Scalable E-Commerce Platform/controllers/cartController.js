const Cart = require('../models/Cart');
const Product = require('../models/Product');

// Get user's cart
exports.getCart = async (req, res) => {
    try {
        const cart = await Cart.findOne({ userId: req.user.id });
        if (!cart) return res.json({ products: [] });
        res.json(cart);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};

// Add product to cart
exports.addToCart = async (req, res) => {
    const { productId, quantity } = req.body;

    try {
        let cart = await Cart.findOne({ userId: req.user.id });

        if (!cart) {
            cart = await Cart.create({ userId: req.user.id, products: [] });
        }

        const productIndex = cart.products.findIndex(p => p.productId.toString() === productId);

        if (productIndex > -1) {
            cart.products[productIndex].quantity += quantity;
        } else {
            cart.products.push({ productId, quantity });
        }

        await cart.save();

        // populate product details for nicer response
        await cart.populate('products.productId');

        res.json(cart);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};


// Remove product from cart
exports.removeFromCart = async (req, res) => {
    const { productId } = req.body;
    try {
        const cart = await Cart.findOne({ userId: req.user.id });
        if (!cart) return res.status(400).json({ message: 'Cart not found' });

        cart.products = cart.products.filter(p => p.productId !== productId);
        await cart.save();
        res.json(cart);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};

// Clear cart
exports.clearCart = async (req, res) => {
    try {
        const cart = await Cart.findOne({ userId: req.user.id });
        if (!cart) return res.status(400).json({ message: 'Cart not found' });

        cart.products = [];
        await cart.save();
        res.json({ message: 'Cart cleared' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};
