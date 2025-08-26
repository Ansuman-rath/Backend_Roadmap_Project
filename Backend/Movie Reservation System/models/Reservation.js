import mongoose from "mongoose";

const reservationSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true },
  showtime: { type: mongoose.Schema.Types.ObjectId, ref: "Showtime", required: true },
  seats: [{ type: Number, required: true }],
  createdAt: { type: Date, default: Date.now },
});

const Reservation = mongoose.model("Reservation", reservationSchema);
export default Reservation;
