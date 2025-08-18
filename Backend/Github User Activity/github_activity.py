#!/usr/bin/env python3
"""
GitHub User Activity CLI
Fetches and displays recent activity of a GitHub user using the GitHub API.
"""

import sys
import json
import urllib.request
import urllib.error
from datetime import datetime
from typing import List, Dict, Any


class GitHubActivityFetcher:
    """Fetches GitHub user activity from the GitHub API."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'GitHub-Activity-CLI/1.0',
            'Accept': 'application/vnd.github.v3+json'
        }
    
    def fetch_user_events(self, username: str) -> List[Dict[str, Any]]:
        """
        Fetch recent events for a GitHub user.
        
        Args:
            username: GitHub username to fetch events for
            
        Returns:
            List of event dictionaries from the GitHub API
            
        Raises:
            urllib.error.HTTPError: If the API request fails
            urllib.error.URLError: If there's a network error
        """
        url = f"{self.BASE_URL}/users/{username}/events"
        
        try:
            request = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(request) as response:
                data = response.read()
                return json.loads(data.decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise ValueError(f"User '{username}' not found on GitHub")
            elif e.code == 403:
                raise ValueError("Rate limit exceeded. Please try again later.")
            else:
                raise ValueError(f"GitHub API error: {e.code} - {e.reason}")
        except urllib.error.URLError as e:
            raise ValueError(f"Network error: {e.reason}")
        except json.JSONDecodeError:
            raise ValueError("Invalid response from GitHub API")


class ActivityFormatter:
    """Formats GitHub events into human-readable text."""
    
    @staticmethod
    def format_event(event: Dict[str, Any]) -> str:
        """
        Format a single GitHub event into a readable string.
        
        Args:
            event: GitHub event dictionary
            
        Returns:
            Formatted string representation of the event
        """
        event_type = event.get('type', 'Unknown')
        repo_name = event.get('repo', {}).get('name', 'Unknown repository')
        
        if event_type == 'PushEvent':
            commits = event.get('payload', {}).get('commits', [])
            commit_count = len(commits)
            if commit_count == 1:
                return f"Pushed 1 commit to {repo_name}"
            else:
                return f"Pushed {commit_count} commits to {repo_name}"
        
        elif event_type == 'CreateEvent':
            ref_type = event.get('payload', {}).get('ref_type', 'item')
            return f"Created a new {ref_type} in {repo_name}"
        
        elif event_type == 'DeleteEvent':
            ref_type = event.get('payload', {}).get('ref_type', 'item')
            return f"Deleted a {ref_type} in {repo_name}"
        
        elif event_type == 'IssuesEvent':
            action = event.get('payload', {}).get('action', 'modified')
            return f"{action.capitalize()} an issue in {repo_name}"
        
        elif event_type == 'IssueCommentEvent':
            action = event.get('payload', {}).get('action', 'created')
            return f"{action.capitalize()} a comment on an issue in {repo_name}"
        
        elif event_type == 'PullRequestEvent':
            action = event.get('payload', {}).get('action', 'opened')
            return f"{action.capitalize()} a pull request in {repo_name}"
        
        elif event_type == 'PullRequestReviewEvent':
            action = event.get('payload', {}).get('action', 'submitted')
            return f"{action.capitalized()} a pull request review in {repo_name}"
        
        elif event_type == 'ForkEvent':
            return f"Forked {repo_name}"
        
        elif event_type == 'WatchEvent':
            action = event.get('payload', {}).get('action', 'watched')
            return f"{action.capitalized()} {repo_name}"
        
        elif event_type == 'StarEvent':
            action = event.get('payload', {}).get('action', 'starred')
            return f"{action.capitalized()} {repo_name}"
        
        elif event_type == 'GistEvent':
            action = event.get('payload', {}).get('action', 'created')
            return f"{action.capitalized()} a gist"
        
        elif event_type == 'CommitCommentEvent':
            return f"Commented on a commit in {repo_name}"
        
        elif event_type == 'ReleaseEvent':
            action = event.get('payload', {}).get('action', 'published')
            return f"{action.capitalized()} a release in {repo_name}"
        
        elif event_type == 'MemberEvent':
            action = event.get('payload', {}).get('action', 'added')
            return f"{action.capitalized()} a member to {repo_name}"
        
        else:
            return f"Performed {event_type} in {repo_name}"
    
    @staticmethod
    def format_events(events: List[Dict[str, Any]], max_events: int = 10) -> str:
        """
        Format a list of GitHub events into a readable string.
        
        Args:
            events: List of GitHub event dictionaries
            max_events: Maximum number of events to display
            
        Returns:
            Formatted string representation of the events
        """
        if not events:
            return "No recent activity found for this user."
        
        # Limit the number of events to display
        events_to_show = events[:max_events]
        
        formatted_events = []
        for event in events_to_show:
            formatted_events.append(f"- {ActivityFormatter.format_event(event)}")
        
        if len(events) > max_events:
            formatted_events.append(f"\n... and {len(events) - max_events} more events")
        
        return "\n".join(formatted_events)


def main():
    """Main function to run the GitHub Activity CLI."""
    
    # Check if username is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        print("Example: python github_activity.py kamranahmedse")
        sys.exit(1)
    
    username = sys.argv[1].strip()
    
    if not username:
        print("Error: Username cannot be empty")
        sys.exit(1)
    
    print(f"Fetching recent activity for GitHub user: {username}")
    print("=" * 50)
    
    try:
        # Fetch user activity
        fetcher = GitHubActivityFetcher()
        events = fetcher.fetch_user_events(username)
        
        # Format and display the activity
        formatter = ActivityFormatter()
        formatted_activity = formatter.format_events(events)
        
        print(formatted_activity)
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
