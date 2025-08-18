# GitHub User Activity CLI

A simple command-line interface (CLI) application that fetches and displays recent activity of a GitHub user using the GitHub API.

## Features

- Fetch recent GitHub user activity without external dependencies
- Human-readable formatting of various GitHub events
- Graceful error handling for invalid usernames and API failures
- Support for multiple event types (pushes, issues, pull requests, stars, etc.)
- Clean, organized output in the terminal

## Requirements

- Python 3.6 or higher
- Internet connection to access the GitHub API

## Installation

No external packages are required! This application uses only Python's built-in libraries:

- `urllib.request` - for HTTP requests
- `json` - for parsing API responses
- `sys` - for command-line argument handling

## Usage

### Basic Usage

```bash
python github_activity.py <username>
```

### Examples

```bash
# Fetch activity for a specific user
python github_activity.py kamranahmedse

# Fetch activity for another user
python github_activity.py torvalds

# Fetch activity for your own username
python github_activity.py yourusername
```

### Output Example

```
Fetching recent activity for GitHub user: kamranahmedse
==================================================
- Pushed 2 commits to kamranahmedse/developer-roadmap
- Opened an issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/awesome-python
- Created a new branch in kamranahmedse/developer-roadmap
- Pushed 1 commit to kamranahmedse/awesome-python
- Forked microsoft/vscode
- Commented on a commit in kamranahmedse/developer-roadmap
- Published a release in kamranahmedse/awesome-python
- Added a member to kamranahmedse/developer-roadmap
- Watched kamranahmedse/awesome-python
```

## Supported Event Types

The application handles various GitHub event types and formats them into readable text:

- **PushEvent** - Code commits pushed to repositories
- **CreateEvent** - New repositories, branches, or tags created
- **DeleteEvent** - Repositories, branches, or tags deleted
- **IssuesEvent** - Issues opened, closed, or modified
- **IssueCommentEvent** - Comments on issues
- **PullRequestEvent** - Pull requests opened, closed, or merged
- **PullRequestReviewEvent** - Pull request reviews submitted
- **ForkEvent** - Repository forks
- **WatchEvent** - Repository watching/unwatching
- **StarEvent** - Repository starring/unstarring
- **GistEvent** - Gist creation, updates, or deletion
- **CommitCommentEvent** - Comments on commits
- **ReleaseEvent** - Repository releases published
- **MemberEvent** - Team members added or removed

## Error Handling

The application gracefully handles various error scenarios:

- **Invalid username**: Displays "User not found" error
- **Rate limiting**: Informs when GitHub API rate limit is exceeded
- **Network errors**: Shows network-related error messages
- **API errors**: Displays specific GitHub API error codes and reasons

## API Endpoint

The application uses the GitHub Events API endpoint:
```
https://api.github.com/users/{username}/events
```

This endpoint provides the most recent 90 days of activity for public users.

## Rate Limiting

GitHub's API has rate limits for unauthenticated requests:
- 60 requests per hour for unauthenticated requests
- 5,000 requests per hour for authenticated requests

If you need to make more requests, consider:
1. Adding authentication to your requests
2. Implementing request caching
3. Respecting the rate limits

## Contributing

Feel free to contribute to this project by:
- Adding support for more event types
- Improving error handling
- Enhancing the output formatting
- Adding new features like filtering or sorting

## License

This project is open source and available under the MIT License.

## Troubleshooting

### Common Issues

1. **"User not found" error**: Verify the username exists and is spelled correctly
2. **Rate limit exceeded**: Wait before making more requests or use authentication
3. **Network errors**: Check your internet connection and firewall settings

### Getting Help

If you encounter issues:
1. Check that the username is valid and exists on GitHub
2. Ensure you have a stable internet connection
3. Verify you're using Python 3.6 or higher
4. Check the error message for specific details

## Future Enhancements

Potential improvements for future versions:
- Authentication support for higher rate limits
- Filtering by event type or repository
- Date range filtering
- JSON output option
- Interactive mode with pagination
- Caching for better performance
