require('dotenv').config();
const mongoose = require('mongoose');
const connectDB = require('./config/db');
const Exercise = require('./models/Exercise');

const exercises = [
    { name: 'Push-up', description: 'Standard push-up', category: 'Strength', muscleGroup: 'Chest' },
    { name: 'Squat', description: 'Bodyweight squat', category: 'Strength', muscleGroup: 'Legs' },
    { name: 'Plank', description: 'Hold plank position', category: 'Strength', muscleGroup: 'Core' },
    { name: 'Running', description: 'Outdoor running', category: 'Cardio', muscleGroup: 'Legs' },
    { name: 'Jumping Jacks', description: 'Full body cardio', category: 'Cardio', muscleGroup: 'Full Body' },
    { name: 'Yoga Stretch', description: 'Flexibility routine', category: 'Flexibility', muscleGroup: 'Full Body' },
];

const seedExercises = async () => {
    try {
        await connectDB();
        await Exercise.deleteMany();
        await Exercise.insertMany(exercises);
        console.log('Exercises seeded successfully');
        process.exit();
    } catch (err) {
        console.error(err);
        process.exit(1);
    }
};

seedExercises();
