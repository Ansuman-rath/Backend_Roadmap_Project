
# Movie Reservation System

This is a **Movie Booking Backend API** built with **Node.js**, **Express**, and **MongoDB**. It allows users to view movies, book showtimes, and provides admin functionality to manage movies and showtimes.

[Movie Reservation System](https://roadmap.sh/projects/movie-reservation-system)
---

## Features

- **User Management**
  - Register and login users
  - JWT-based authentication
  - Role-based access (Admin/User)

- **Movie Management**
  - Admin can add, update, and delete movies
  - Users can view movies

- **Showtime Management**
  - Admin can add showtimes for movies
  - Users can view showtimes
  - Capacity management for each showtime

- **Booking**
  - Users can book seats for available showtimes
  - Booking validation based on capacity

---

## Technologies Used

- **Node.js** – JavaScript runtime
- **Express.js** – Web framework
- **MongoDB** – NoSQL database
- **Mongoose** – MongoDB ODM
- **JWT** – Authentication
- **bcryptjs** – Password hashing
- **Nodemon** – Development tool for auto-restart

---

## Project Structure

```

movie-booking-api/
│
├── controllers/
│   ├── movieController.js
│   ├── showtimeController.js
│   └── userController.js
│
├── middleware/
│   └── authMiddleware.js
│
├── models/
│   ├── Movie.js
│   ├── Showtime.js
│   └── User.js
│
├── routes/
│   ├── movieRoutes.js
│   ├── showtimeRoutes.js
│   └── userRoutes.js
│
├── server.js
├── package.json
└── .env

````

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/Ansuman-rath/Backend_Roadmap_Project
cd Movie Reservation System
````

2. Install dependencies:

```bash
npm install
```

3. Create a `.env` file in the root directory with:

```env
PORT=5000
MONGO_URI=<your_mongodb_connection_string>
JWT_SECRET=<your_jwt_secret>
```

4. Start the server:

```bash
npm run dev
```

The server will start on `http://localhost:5000`.

---

## API Endpoints

### User

* `POST /api/users/register` – Register a new user
* `POST /api/users/login` – Login and get JWT token
* `GET /api/users/profile` – Get user profile (protected)

### Movies

* `GET /api/movies` – List all movies
* `POST /api/movies` – Add a movie (admin only)
* `PUT /api/movies/:id` – Update a movie (admin only)
* `DELETE /api/movies/:id` – Delete a movie (admin only)

### Showtimes

* `GET /api/showtime` – List all showtimes
* `POST /api/showtime` – Add a showtime (admin only)

---

## Notes

* All **protected routes** require the `Authorization: Bearer <token>` header.
* Admin users are required to manage movies and showtimes.
* Ensure MongoDB is running and `.env` variables are set properly.
