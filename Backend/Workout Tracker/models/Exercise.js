const mongoose = require('mongoose');

const exerciseSchema = new mongoose.Schema({
    name: { type: String, required: true },
    description: { type: String },
    category: { type: String, enum: ['Cardio', 'Strength', 'Flexibility'], required: true },
    muscleGroup: { type: String } // e.g., Chest, Back, Legs
}, { timestamps: true });

module.exports = mongoose.model('Exercise', exerciseSchema);
