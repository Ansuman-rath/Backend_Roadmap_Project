import mongoose from "mongoose";

const scoreSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: "User", index: true },
  gameId: { type: String, index: true },
  score: Number
}, { timestamps: { createdAt: true, updatedAt: false } });

export default mongoose.model("Score", scoreSchema);
