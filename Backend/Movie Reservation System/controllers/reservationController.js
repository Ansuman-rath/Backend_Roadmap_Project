import Reservation from "../models/Reservation.js";
import Showtime from "../models/Showtime.js";

export const createReservation = async (req, res) => {
  const { showtimeId, seats } = req.body;
  const showtime = await Showtime.findById(showtimeId);

  const alreadyReserved = seats.some((s) => showtime.reservedSeats.includes(s));
  if (alreadyReserved) return res.status(400).json({ message: "Seat already taken" });

  showtime.reservedSeats.push(...seats);
  await showtime.save();

  const reservation = await Reservation.create({
    user: req.user._id,
    showtime: showtimeId,
    seats,
  });

  res.json(reservation);
};

export const getUserReservations = async (req, res) => {
  const reservations = await Reservation.find({ user: req.user._id }).populate("showtime");
  res.json(reservations);
};

export const cancelReservation = async (req, res) => {
  const reservation = await Reservation.findById(req.params.id);
  if (!reservation) return res.status(404).json({ message: "Reservation not found" });
  if (reservation.user.toString() !== req.user._id.toString())
    return res.status(403).json({ message: "Not your reservation" });

  const showtime = await Showtime.findById(reservation.showtime);
  showtime.reservedSeats = showtime.reservedSeats.filter((s) => !reservation.seats.includes(s));
  await showtime.save();

  await reservation.deleteOne();
  res.json({ message: "Reservation canceled" });
};
