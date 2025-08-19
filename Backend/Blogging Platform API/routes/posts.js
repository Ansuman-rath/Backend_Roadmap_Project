const express = require('express');
const { runQuery, getRow, getAll } = require('../database/database');
const { validatePost } = require('../middleware/validation');

const router = express.Router();

// Helper function to format post data
function formatPost(post) {
  return {
    id: post.id,
    title: post.title,
    content: post.content,
    category: post.category,
    tags: JSON.parse(post.tags),
    createdAt: post.createdAt,
    updatedAt: post.updatedAt
  };
}

// CREATE - POST /posts
router.post('/', validatePost, async (req, res) => {
  try {
    const { title, content, category, tags } = req.body;
    
    // Store tags as JSON string in database
    const tagsJson = JSON.stringify(tags);
    
    const sql = `
      INSERT INTO posts (title, content, category, tags, createdAt, updatedAt)
      VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))
    `;
    
    const result = await runQuery(sql, [title, content, category, tagsJson]);
    
    // Get the created post
    const createdPost = await getRow('SELECT * FROM posts WHERE id = ?', [result.id]);
    
    res.status(201).json(formatPost(createdPost));
  } catch (error) {
    console.error('Error creating post:', error);
    res.status(500).json({
      error: 'Internal Server Error',
      message: 'Failed to create blog post'
    });
  }
});

// READ ALL - GET /posts (with optional search)
router.get('/', async (req, res) => {
  try {
    const { term } = req.query;
    let sql, params;
    
    if (term) {
      // Search in title, content, and category
      sql = `
        SELECT * FROM posts 
        WHERE title LIKE ? OR content LIKE ? OR category LIKE ?
        ORDER BY createdAt DESC
      `;
      const searchTerm = `%${term}%`;
      params = [searchTerm, searchTerm, searchTerm];
    } else {
      // Get all posts
      sql = 'SELECT * FROM posts ORDER BY createdAt DESC';
      params = [];
    }
    
    const posts = await getAll(sql, params);
    const formattedPosts = posts.map(formatPost);
    
    res.status(200).json(formattedPosts);
  } catch (error) {
    console.error('Error fetching posts:', error);
    res.status(500).json({
      error: 'Internal Server Error',
      message: 'Failed to fetch blog posts'
    });
  }
});

// READ ONE - GET /posts/:id
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    
    // Validate ID parameter
    if (isNaN(id) || parseInt(id) <= 0) {
      return res.status(400).json({
        error: 'Bad Request',
        message: 'Invalid post ID'
      });
    }
    
    const post = await getRow('SELECT * FROM posts WHERE id = ?', [id]);
    
    if (!post) {
      return res.status(404).json({
        error: 'Not Found',
        message: 'Blog post not found'
      });
    }
    
    res.status(200).json(formatPost(post));
  } catch (error) {
    console.error('Error fetching post:', error);
    res.status(500).json({
      error: 'Internal Server Error',
      message: 'Failed to fetch blog post'
    });
  }
});

// UPDATE - PUT /posts/:id
router.put('/:id', validatePost, async (req, res) => {
  try {
    const { id } = req.params;
    const { title, content, category, tags } = req.body;
    
    // Validate ID parameter
    if (isNaN(id) || parseInt(id) <= 0) {
      return res.status(400).json({
        error: 'Bad Request',
        message: 'Invalid post ID'
      });
    }
    
    // Check if post exists
    const existingPost = await getRow('SELECT * FROM posts WHERE id = ?', [id]);
    if (!existingPost) {
      return res.status(404).json({
        error: 'Not Found',
        message: 'Blog post not found'
      });
    }
    
    // Store tags as JSON string in database
    const tagsJson = JSON.stringify(tags);
    
    const sql = `
      UPDATE posts 
      SET title = ?, content = ?, category = ?, tags = ?, updatedAt = datetime('now')
      WHERE id = ?
    `;
    
    await runQuery(sql, [title, content, category, tagsJson, id]);
    
    // Get the updated post
    const updatedPost = await getRow('SELECT * FROM posts WHERE id = ?', [id]);
    
    res.status(200).json(formatPost(updatedPost));
  } catch (error) {
    console.error('Error updating post:', error);
    res.status(500).json({
      error: 'Internal Server Error',
      message: 'Failed to update blog post'
    });
  }
});

// DELETE - DELETE /posts/:id
router.delete('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    
    // Validate ID parameter
    if (isNaN(id) || parseInt(id) <= 0) {
      return res.status(400).json({
        error: 'Bad Request',
        message: 'Invalid post ID'
      });
    }
    
    // Check if post exists
    const existingPost = await getRow('SELECT * FROM posts WHERE id = ?', [id]);
    if (!existingPost) {
      return res.status(404).json({
        error: 'Not Found',
        message: 'Blog post not found'
      });
    }
    
    // Delete the post
    await runQuery('DELETE FROM posts WHERE id = ?', [id]);
    
    res.status(204).send();
  } catch (error) {
    console.error('Error deleting post:', error);
    res.status(500).json({
      error: 'Internal Server Error',
      message: 'Failed to delete blog post'
    });
  }
});

module.exports = router;
