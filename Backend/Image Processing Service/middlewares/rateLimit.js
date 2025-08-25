const rateLimit = require('express-rate-limit');

const transformLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 min
  max: 5,
  message: "Too many transformations, please try again later"
});

module.exports = { transformLimiter };
