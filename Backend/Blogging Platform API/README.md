# Blogging Platform API

A RESTful API for a personal blogging platform built with Node.js, Express.js, and SQLite.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete blog posts
- **Search Functionality**: Filter posts by search terms across title, content, and category
- **Data Validation**: Comprehensive input validation with detailed error messages
- **RESTful Design**: Follows REST API best practices and conventions
- **Error Handling**: Proper HTTP status codes and error responses
- **Security**: Helmet.js for security headers, CORS enabled

## Tech Stack

- **Runtime**: Node.js
- **Framework**: Express.js
- **Database**: SQLite3
- **Security**: Helmet.js
- **Logging**: Morgan
- **CORS**: Enabled for cross-origin requests

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blogging-platform-api
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the server**
   ```bash
   # Production
   npm start
   
   # Development (with auto-reload)
   npm run dev
   ```

The API will be available at `http://localhost:3000`

## API Endpoints

### Health Check
- **GET** `/health` - Check API status

### Blog Posts

#### Create Blog Post
- **POST** `/posts`
- **Body**:
  ```json
  {
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"]
  }
  ```
- **Response**: `201 Created` with the created post
- **Validation**: All fields are required and validated

#### Get All Blog Posts
- **GET** `/posts`
- **Query Parameters**:
  - `term` (optional): Search term for filtering posts
- **Response**: `200 OK` with array of posts
- **Example**: `GET /posts?term=tech`

#### Get Single Blog Post
- **GET** `/posts/:id`
- **Response**: `200 OK` with the post or `404 Not Found`

#### Update Blog Post
- **PUT** `/posts/:id`
- **Body**: Same as create post
- **Response**: `200 OK` with updated post or `404 Not Found`

#### Delete Blog Post
- **DELETE** `/posts/:id`
- **Response**: `204 No Content` on success or `404 Not Found`

## Data Model

### Blog Post Structure
```json
{
  "id": 1,
  "title": "Post Title",
  "content": "Post content...",
  "category": "Category Name",
  "tags": ["tag1", "tag2"],
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z"
}
```

### Database Schema
- `id`: Auto-incrementing primary key
- `title`: Post title (max 255 characters)
- `content`: Post content (unlimited)
- `category`: Post category (max 100 characters)
- `tags`: JSON array of tags (stored as JSON string)
- `createdAt`: Creation timestamp
- `updatedAt`: Last update timestamp

## Validation Rules

- **Title**: Required, non-empty string, max 255 characters
- **Content**: Required, non-empty string
- **Category**: Required, non-empty string, max 100 characters
- **Tags**: Required array with at least one tag, each tag max 50 characters

## Error Handling

The API returns appropriate HTTP status codes:

- `200 OK`: Successful GET/PUT requests
- `201 Created`: Successful POST requests
- `204 No Content`: Successful DELETE requests
- `400 Bad Request`: Validation errors
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server errors

### Error Response Format
```json
{
  "error": "Error Type",
  "message": "Human readable message",
  "details": ["Detailed error messages"]
}
```

## Search Functionality

The search feature performs wildcard searches across:
- Post title
- Post content
- Post category

Search is case-insensitive and uses SQL LIKE queries with `%term%` pattern.

## Usage Examples

### Using cURL

1. **Create a post**
   ```bash
   curl -X POST http://localhost:3000/posts \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Getting Started with Node.js",
       "content": "Node.js is a powerful JavaScript runtime...",
       "category": "Programming",
       "tags": ["Node.js", "JavaScript", "Backend"]
     }'
   ```

2. **Get all posts**
   ```bash
   curl http://localhost:3000/posts
   ```

3. **Search posts**
   ```bash
   curl "http://localhost:3000/posts?term=javascript"
   ```

4. **Update a post**
   ```bash
   curl -X PUT http://localhost:3000/posts/1 \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Updated Title",
       "content": "Updated content...",
       "category": "Programming",
       "tags": ["Node.js", "JavaScript"]
     }'
   ```

5. **Delete a post**
   ```bash
   curl -X DELETE http://localhost:3000/posts/1
   ```

### Using JavaScript/Fetch

```javascript
// Create a post
const response = await fetch('http://localhost:3000/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: 'My Blog Post',
    content: 'Post content here...',
    category: 'Technology',
    tags: ['Tech', 'Blog']
  })
});

const post = await response.json();
```

## Development

### Project Structure
```
blogging-platform-api/
├── database/
│   └── database.js          # Database configuration and helpers
├── middleware/
│   └── validation.js        # Input validation middleware
├── routes/
│   └── posts.js            # Blog post routes
├── server.js               # Main server file
├── package.json            # Dependencies and scripts
└── README.md              # This file
```

### Database
- SQLite database file is automatically created at `database/blog.db`
- Tables and indexes are created on first run
- No manual database setup required

### Adding New Features
- Add new routes in the `routes/` directory
- Create new middleware in the `middleware/` directory
- Update database schema in `database/database.js`

## Testing

The API can be tested using:
- **Postman**: Import the endpoints and test manually
- **cURL**: Command-line testing as shown in examples
- **Browser**: For GET requests
- **Any HTTP client**: The API follows standard REST conventions

## Deployment

1. Set environment variables:
   - `PORT`: Server port (default: 3000)

2. Install production dependencies:
   ```bash
   npm install --production
   ```

3. Start the server:
   ```bash
   npm start
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions, please open an issue on the repository.
