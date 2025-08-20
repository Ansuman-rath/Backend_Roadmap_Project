#!/usr/bin/env node
const express = require("express");
const axios = require("axios");
const { Command } = require("commander");

const program = new Command();
let cache = {};

// CLI definition
program
  .option("--port <number>", "Port for proxy server", "3000")
  .option("--origin <url>", "Origin server URL")
  .option("--clear-cache", "Clear the cache")
  .parse(process.argv);

const options = program.opts();

// Handle cache clearing
if (options.clearCache) {
  cache = {};
  console.log("✅ Cache cleared successfully!");
  process.exit(0);
}

if (!options.origin) {
  console.error("❌ Error: --origin is required when starting the server");
  process.exit(1);
}

const app = express();
const PORT = options.port;
const ORIGIN = options.origin;

// Proxy route (catch-all)
app.use(async (req, res) => {
  const cacheKey = req.originalUrl;

  // If response is cached
  if (cache[cacheKey]) {
    const { data, headers, status } = cache[cacheKey];
    res.set(headers);
    res.set("X-Cache", "HIT");
    return res.status(status).send(data);
  }

  // Otherwise, fetch from origin
  try {
    const response = await axios.get(`${ORIGIN}${req.originalUrl}`, {
        headers: {
          ...req.headers,
          host: new URL(ORIGIN).host,   // force correct Host header
        }
      });
      
    

    // Store in cache
    cache[cacheKey] = {
      data: response.data,
      headers: response.headers,
      status: response.status
    };

    res.set(response.headers);
    res.set("X-Cache", "MISS");
    res.status(response.status).send(response.data);
  } catch (err) {
    if (err.response) {
      res.status(err.response.status).send(err.response.data);
    } else {
      res.status(500).send("Error connecting to origin server");
    }
  }
});

app.listen(PORT, () => {
  console.log(`🚀 Caching proxy server running on http://localhost:${PORT}`);
  console.log(`🔗 Forwarding requests to: ${ORIGIN}`);
});
