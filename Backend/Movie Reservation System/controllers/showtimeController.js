import Showtime from "../models/Showtime.js";

export const addShowtime = async (req, res) => {
  const showtime = await Showtime.create(req.body);
  res.json(showtime);
};

export const getShowtimes = async (req, res) => {
  const showtimes = await Showtime.find().populate("movie");
  res.json(showtimes);
};
