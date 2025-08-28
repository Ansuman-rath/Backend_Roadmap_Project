import redis from "redis";

export const redisClient = redis.createClient({
  url: process.env.REDIS_URL || "redis://127.0.0.1:6379",
});

redisClient.on("error", (err) => console.log("Redis Client Error:", err));
redisClient.on("ready", () => console.log("Redis Connected"));

async function connectRedis() {
  try {
    await redisClient.connect();
  } catch (err) {
    console.log("Redis connection failed:", err);
  }
}

connectRedis();
