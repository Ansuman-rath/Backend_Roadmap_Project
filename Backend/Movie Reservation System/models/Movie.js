import mongoose from "mongoose";

const movieSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String },
  genre: { type: String },
  poster: { type: String },
});

const Movie = mongoose.model("Movie", movieSchema);
export default Movie;
