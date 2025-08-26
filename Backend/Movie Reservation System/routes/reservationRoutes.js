import express from "express";
import { createReservation, getUserReservations, cancelReservation } from "../controllers/reservationController.js";
import { protect } from "../middleware/authMiddleware.js";

const router = express.Router();

router.post("/", protect, createReservation);
router.get("/", protect, getUserReservations);
router.delete("/:id", protect, cancelReservation);

export default router;
