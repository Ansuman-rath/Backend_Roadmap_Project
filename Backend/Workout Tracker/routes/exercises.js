const express = require('express');
const router = express.Router();
const Exercise = require('../models/Exercise');

// Get all exercises
router.get('/', async (req, res) => {
    try {
        const exercises = await Exercise.find();
        res.json(exercises);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
});

// Optionally: add a new exercise (admin)
router.post('/', async (req, res) => {
    const { name, description, category, muscleGroup } = req.body;
    try {
        const exercise = new Exercise({ name, description, category, muscleGroup });
        await exercise.save();
        res.json(exercise);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
});

module.exports = router;
