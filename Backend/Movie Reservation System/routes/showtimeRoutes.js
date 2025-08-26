import express from "express";
import { addShowtime, getShowtimes } from "../controllers/showtimeController.js";
import { protect, admin } from "../middleware/authMiddleware.js";

const router = express.Router();

router.get("/", getShowtimes);
router.post("/", protect, admin, addShowtime);

export default router;
