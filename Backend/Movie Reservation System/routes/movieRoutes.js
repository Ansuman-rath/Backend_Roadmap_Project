import express from "express";
import { addMovie, getMovies, updateMovie, deleteMovie } from "../controllers/movieController.js";
import { protect, admin } from "../middleware/authMiddleware.js";

const router = express.Router();

router.get("/", getMovies);
router.post("/", protect, admin, addMovie);
router.put("/:id", protect, admin, updateMovie);
router.delete("/:id", protect, admin, deleteMovie);

export default router;
