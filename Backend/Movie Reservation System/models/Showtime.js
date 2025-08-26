import mongoose from "mongoose";

const showtimeSchema = new mongoose.Schema({
  movie: { type: mongoose.Schema.Types.ObjectId, ref: "Movie", required: true },
  startTime: { type: Date, required: true },
  totalSeats: { type: Number, required: true },
  reservedSeats: [{ type: Number }], // e.g. seat numbers
});

const Showtime = mongoose.model("Showtime", showtimeSchema);
export default Showtime;
