# Leaderboard API Project

A Node.js REST API for managing a leaderboard with fast, real-time scoring using **Redis**. Users can submit scores, view their rank, and fetch the top players.

[Real-time Leaderboard](https://roadmap.sh/projects/realtime-leaderboard-system)

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Installation](#installation)
4. [Environment Variables](#environment-variables)
5. [API Endpoints](#api-endpoints)
6. [Usage](#usage)
7. [Notes](#notes)

---

## Features

* Add or update user scores.
* Get the top 10 users on the leaderboard.
* Fetch a specific user’s rank and score.
* Fast and efficient with Redis sorted sets.

---

## Tech Stack

* **Node.js** – backend runtime
* **Express** – REST API framework
* **Redis** – in-memory data store for leaderboard
* **Nodemon** – for development hot-reloading

> MongoDB is not required for leaderboard functionality, but can optionally be used for persisting user info.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Ansuman-rath/Backend_Roadmap_Project
cd Real-time Leaderboard
```

2. Install dependencies:

```bash
npm install
```

3. Make sure Redis is installed and running. For local setup:

```bash
redis-server
```

4. Start the server:

```bash
npm run dev
```

You should see:

```
Redis Connected
Server running on port 5000
```

---

## Environment Variables

Create a `.env` file in the root:

```env
PORT=5000
REDIS_URL=redis://127.0.0.1:6379
```

* `PORT` – the port your server will run on.
* `REDIS_URL` – Redis connection URL.

---

## API Endpoints

### 1. Add or Update Score

* **POST** `/api/leaderboard/`
* **Body:**

```json
{
  "username": "alice",
  "score": 250
}
```

* **Response:**

```json
{
  "message": "Score added/updated successfully"
}
```

---

### 2. Get Top 10 Leaderboard

* **GET** `/api/leaderboard/`
* **Response:**

```json
[
  { "username": "alice", "score": 250 },
  { "username": "bob", "score": 200 },
  ...
]
```

---

### 3. Get User Rank

* **GET** `/api/leaderboard/:username`
* **Example:** `/api/leaderboard/alice`
* **Response:**

```json
{
  "username": "alice",
  "rank": 1,
  "score": 250
}
```

* Returns `404` if the user is not found.

---

## Usage

1. Use **Postman** or any HTTP client to interact with the API.
2. Start by posting scores for users.
3. Fetch the leaderboard or a specific user’s rank.

---

## Notes

* Redis stores data in memory, so data is lost if the server or Redis restarts (unless you configure persistence).
* The leaderboard is sorted in descending order (highest score first).
* Redis **sorted sets** are used, which allows efficient score updates and rank queries.
