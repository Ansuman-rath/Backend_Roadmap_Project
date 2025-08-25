const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const Workout = require('../models/Workout');

// Create Workout
router.post('/', auth, async (req, res) => {
    const { name, comments, exercises, scheduledFor } = req.body;
    try {
        const workout = new Workout({
            userId: req.user.id,
            name,
            comments,
            exercises,
            scheduledFor
        });
        await workout.save();
        res.json(workout);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
});

// Get all workouts for logged-in user
router.get('/', auth, async (req, res) => {
    try {
        const workouts = await Workout.find({ userId: req.user.id }).populate('exercises.exerciseId', 'name category muscleGroup');
        res.json(workouts);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
});

// Get a specific workout
router.get('/:id', auth, async (req, res) => {
    try {
        const workout = await Workout.findOne({ _id: req.params.id, userId: req.user.id }).populate('exercises.exerciseId', 'name category muscleGroup');
        if (!workout) return res.status(404).json({ msg: 'Workout not found' });
        res.json(workout);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
});

// Update workout
router.put('/:id', auth, async (req, res) => {
    try {
        const workout = await Workout.findOneAndUpdate(
            { _id: req.params.id, userId: req.user.id },
            { $set: req.body },
            { new: true }
        );
        if (!workout) return res.status(404).json({ msg: 'Workout not found' });
        res.json(workout);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
});

// Delete workout
router.delete('/:id', auth, async (req, res) => {
    try {
        const workout = await Workout.findOneAndDelete({ _id: req.params.id, userId: req.user.id });
        if (!workout) return res.status(404).json({ msg: 'Workout not found' });
        res.json({ msg: 'Workout deleted' });
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
});

module.exports = router;
