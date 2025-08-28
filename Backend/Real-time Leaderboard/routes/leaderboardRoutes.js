import express from "express";
import { getLeaderboard, getUserRank, addScore } from "../controllers/leaderboardController.js";

const router = express.Router();

router.get("/", getLeaderboard);          // Get top 10 leaderboard
router.get("/:username", getUserRank);    // Get rank of specific user
router.post("/", addScore);               // Add or update score

export default router;
