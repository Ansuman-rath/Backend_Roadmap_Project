
# Workout Tracker API


A **Node.js + Express + MongoDB backend API** for tracking workouts, exercises, and user progress. Users can sign up, log in, create workout plans, schedule workouts, and generate reports on their progress.

[Workout Tracker](https://roadmap.sh/projects/fitness-workout-tracker)

---

## **Features**

* **User Authentication**: Signup, Login with JWT authentication.
* **Exercises**: List all exercises, add new exercises.
* **Workouts**: Create, update, delete, and list workouts with multiple exercises.
* **Workout Scheduling**: Schedule workouts for specific dates and times.
* **Reports**: Generate user-specific progress reports, including total workouts, exercises completed, and upcoming workouts.

---

## **Tech Stack**

* Node.js + Express
* MongoDB + Mongoose
* JWT Authentication
* Bcrypt for password hashing
* Postman for testing API endpoints

---

## **Project Structure**

```
workout-tracker/
│
├─ index.js              # Entry point
├─ .env                  # Environment variables
├─ config/
│   └─ db.js             # MongoDB connection
├─ models/
│   ├─ User.js           # User model
│   ├─ Exercise.js       # Exercise model
│   └─ Workout.js        # Workout model
├─ routes/
│   ├─ auth.js           # Signup/Login routes
│   ├─ exercises.js      # Exercise routes
│   ├─ workouts.js       # Workout routes
│   └─ reports.js        # Reports route
└─ middleware/
    └─ auth.js           # JWT authentication middleware
```

---

## **Setup Instructions**

### **1. Clone the repository**

```bash
git clone https://github.com/Ansuman-rath/Backend_Roadmap_Project
cd Workout Tracker
```

### **2. Install dependencies**

```bash
npm install
```

### **3. Create `.env` file**

```env
PORT=5000
MONGO_URI=your_mongo_connection
JWT_SECRET=your_jwt_secret
```

### **4. Seed Exercises**

```bash
node seedExercises.js
```

### **5. Start Server**

```bash
npm run dev
```

Server runs at: `http://localhost:5000`

---

## **API Endpoints**

### **Authentication**

* `POST /auth/signup` → Sign up
* `POST /auth/login` → Login, returns JWT

### **Exercises**

* `GET /exercises` → List all exercises
* `POST /exercises` → Add a new exercise (optional)

### **Workouts**

* `POST /workouts` → Create workout
* `GET /workouts` → List all user workouts
* `GET /workouts/:id` → Get a specific workout
* `PUT /workouts/:id` → Update workout
* `DELETE /workouts/:id` → Delete workout

### **Reports**

* `GET /reports` → User progress report (total workouts, exercises, upcoming workouts)

---

## **Sample Request & Response**

**Create Workout**

```http
POST /workouts
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "name": "Morning Routine",
  "comments": "Focus on chest and legs",
  "exercises": [
    { "exerciseId": "<exercise_id>", "sets": 3, "reps": 12, "weight": 0 }
  ],
  "scheduledFor": "2025-08-26T07:00:00.000Z"
}
```

**Response**

```json
{
  "_id": "workout_id_here",
  "userId": "user_id_here",
  "name": "Morning Routine",
  "comments": "Focus on chest and legs",
  "exercises": [...],
  "scheduledFor": "2025-08-26T07:00:00.000Z",
  "createdAt": "...",
  "updatedAt": "..."
}
```

---

## **Testing**

* Use **Postman** to test endpoints.
* Include JWT token in **Authorization header** for protected routes.

