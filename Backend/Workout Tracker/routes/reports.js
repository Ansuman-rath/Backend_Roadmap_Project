const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const Workout = require('../models/Workout');

// GET /reports - User progress report
router.get('/', auth, async (req, res) => {
    try {
        const userId = req.user.id;

        // Total workouts
        const totalWorkouts = await Workout.countDocuments({ userId });

        // Total exercises done
        const workouts = await Workout.find({ userId });
        let totalExercises = 0;
        let exercisesByMuscle = {};

        workouts.forEach(workout => {
            workout.exercises.forEach(ex => {
                totalExercises += 1;

                // Count by muscle group
                if (ex.exerciseId.muscleGroup) {
                    const muscle = ex.exerciseId.muscleGroup;
                    exercisesByMuscle[muscle] = (exercisesByMuscle[muscle] || 0) + ex.sets;
                }
            });
        });

        // Scheduled workouts
        const now = new Date();
        const upcomingWorkouts = await Workout.find({ userId, scheduledFor: { $gt: now } }).sort({ scheduledFor: 1 });

        res.json({
            totalWorkouts,
            totalExercises,
            exercisesByMuscle,
            upcomingWorkouts: upcomingWorkouts.map(w => ({
                name: w.name,
                scheduledFor: w.scheduledFor
            }))
        });

    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
});

module.exports = router;
