const mongoose = require('mongoose');

const workoutSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    name: { type: String, required: true },
    comments: { type: String },
    exercises: [
        {
            exerciseId: { type: mongoose.Schema.Types.ObjectId, ref: 'Exercise', required: true },
            sets: { type: Number, required: true },
            reps: { type: Number, required: true },
            weight: { type: Number, default: 0 }
        }
    ],
    scheduledFor: { type: Date },
}, { timestamps: true });

module.exports = mongoose.model('Workout', workoutSchema);
