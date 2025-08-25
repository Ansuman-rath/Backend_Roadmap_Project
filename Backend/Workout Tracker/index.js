require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const connectDB = require('./config/db');

const app = express();
connectDB();

app.use(bodyParser.json());

// Routes
app.use('/auth', require('./routes/auth'));
app.use('/exercises', require('./routes/exercises'));
app.use('/workouts', require('./routes/workouts'));
app.use('/reports', require('./routes/reports'));


const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
