import { redisClient } from "../config/redis.js";

export const submitScore = async (req, res) => {
  const { score } = req.body;
  const username = req.user.username;

  try {
    // Add to Redis leaderboard
    await redisClient.zAdd("globalLeaderboard", {
      score: score,
      value: username,
    });

    res.json({ message: "Score submitted", username, score });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};
