
# Scalable E-Commerce Platform

A RESTful API for an e-commerce platform, built with **Node.js**, **Express**, and **MongoDB**. This API allows user authentication, product management, cart functionality, and order processing.

[Scalable E-Commerce Platform](https://roadmap.sh/projects/scalable-ecommerce-platform)
---

## Features

* **User Management**

  * Register new users
  * Login with JWT authentication
  * Admin role validation

* **Product Management**

  * Create, read, update, and delete products (Admin only)
  * List all products

* **Cart Management**

  * Add products to cart
  * Remove products from cart
  * Clear cart
  * View current cart

* **Order Management**

  * Place an order
  * View user orders
  * Admin can view all orders and update order status

---

## Technologies Used

* Node.js
* Express.js
* MongoDB (Atlas)
* Mongoose ODM
* JSON Web Tokens (JWT)
* bcrypt for password hashing
* Postman for API testing

---

## Project Structure

```
project-root/
│
├─ config/
│   └─ db.js             # MongoDB connection
│
├─ controllers/
│   ├─ authController.js
│   ├─ productController.js
│   ├─ cartController.js
│   └─ orderController.js
│
├─ middleware/
│   └─ authMiddleware.js
│
├─ models/
│   ├─ User.js
│   ├─ Product.js
│   ├─ Cart.js
│   └─ Order.js
│
├─ routes/
│   ├─ auth.js
│   ├─ products.js
│   ├─ cart.js
│   └─ orders.js
│
├─ server.js
└─ .env                 # Environment variables
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Ansuman-rath/Backend_Roadmap_Project
cd Scalable E-Commerce Platform
```

2. Install dependencies:

```bash
npm install
```

3. Set up environment variables in `.env`:

```
PORT=5000
MONGO_URI=<your_mongodb_connection_string>
JWT_SECRET=<your_jwt_secret>
```

4. Start the server:

```bash
npm start
```

Server runs on `http://localhost:5000`.

---

## API Endpoints

### Auth

* `POST /api/auth/register` — Register a new user
* `POST /api/auth/login` — Login user and get JWT

### Products

* `GET /api/products` — Get all products
* `POST /api/products` — Create a new product (Admin only)
* `PUT /api/products/:id` — Update product (Admin only)
* `DELETE /api/products/:id` — Delete product (Admin only)

### Cart

* `GET /api/cart` — Get current user’s cart
* `POST /api/cart/add` — Add product to cart
* `POST /api/cart/remove` — Remove product from cart
* `POST /api/cart/clear` — Clear the cart

### Orders

* `POST /api/orders` — Place an order
* `GET /api/orders` — Get user orders
* `PUT /api/orders/:id` — Update order status (Admin only)

---

## Testing

* Tested using **Postman** for all endpoints
* Verified JWT authentication and admin-only routes
* Cart and orders tested with multiple products and quantities
* CRUD operations verified for products
