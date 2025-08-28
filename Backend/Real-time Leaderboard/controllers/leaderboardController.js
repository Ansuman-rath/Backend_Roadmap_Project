import { redisClient } from "../config/redis.js";

// Get top 10 users
export const getLeaderboard = async (req, res) => {
  try {
    // Use zRevRangeWithScores for reverse order with scores
    const topUsers = await redisClient.zRevRangeWithScores("leaderboard", 0, 9);

    // Format array into [{ username, score }, ...]
    const formatted = topUsers.map((user) => ({
      username: user.value,
      score: user.score,
    }));

    res.json(formatted);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

// Get specific user's rank
export const getUserRank = async (req, res) => {
  try {
    const { username } = req.params;
    const rank = await redisClient.zRevRank("leaderboard", username); // 0-based
    if (rank === null) return res.status(404).json({ message: "User not found" });

    const score = await redisClient.zScore("leaderboard", username);
    res.json({ username, rank: rank + 1, score: Number(score) });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

// Add or update user score
export const addScore = async (req, res) => {
  try {
    const { username, score } = req.body;
    if (!username || score == null) {
      return res.status(400).json({ message: "Username and score required" });
    }

    await redisClient.zAdd("leaderboard", [{ score: Number(score), value: username }]);

    res.json({ message: "Score added/updated successfully" });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};
