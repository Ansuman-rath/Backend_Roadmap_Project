// Validation middleware for blog posts
function validatePost(req, res, next) {
  const { title, content, category, tags } = req.body;
  const errors = [];

  // Validate title
  if (!title || typeof title !== 'string' || title.trim().length === 0) {
    errors.push('Title is required and must be a non-empty string');
  } else if (title.length > 255) {
    errors.push('Title must be less than 255 characters');
  }

  // Validate content
  if (!content || typeof content !== 'string' || content.trim().length === 0) {
    errors.push('Content is required and must be a non-empty string');
  }

  // Validate category
  if (!category || typeof category !== 'string' || category.trim().length === 0) {
    errors.push('Category is required and must be a non-empty string');
  } else if (category.length > 100) {
    errors.push('Category must be less than 100 characters');
  }

  // Validate tags
  if (!tags || !Array.isArray(tags)) {
    errors.push('Tags must be an array');
  } else if (tags.length === 0) {
    errors.push('At least one tag is required');
  } else {
    // Validate each tag
    for (let i = 0; i < tags.length; i++) {
      const tag = tags[i];
      if (typeof tag !== 'string' || tag.trim().length === 0) {
        errors.push(`Tag at index ${i} must be a non-empty string`);
      } else if (tag.length > 50) {
        errors.push(`Tag at index ${i} must be less than 50 characters`);
      }
    }
  }

  // If there are validation errors, return 400 Bad Request
  if (errors.length > 0) {
    return res.status(400).json({
      error: 'Validation Error',
      message: 'Invalid request data',
      details: errors
    });
  }

  // Sanitize the data
  req.body.title = title.trim();
  req.body.content = content.trim();
  req.body.category = category.trim();
  req.body.tags = tags.map(tag => tag.trim());

  next();
}

module.exports = {
  validatePost
};
