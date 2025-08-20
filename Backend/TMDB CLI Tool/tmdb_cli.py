#!/usr/bin/env python3
"""
TMDB CLI Tool
A command line interface to fetch movie information from The Movie Database (TMDB)
"""

import os
import sys
import click
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Rich console
console = Console()

# TMDB API configuration
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Movie type endpoints mapping
MOVIE_ENDPOINTS = {
    "playing": "/movie/now_playing",
    "popular": "/movie/popular",
    "top": "/movie/top_rated",
    "upcoming": "/movie/upcoming"
}

def get_api_key():
    """Get TMDB API key from environment or prompt user"""
    if not TMDB_API_KEY:
        console.print("[red]Error: TMDB_API_KEY environment variable not set![/red]")
        console.print("Please set your TMDB API key in a .env file or as an environment variable.")
        console.print("You can get a free API key from: https://www.themoviedb.org/settings/api")
        sys.exit(1)
    return TMDB_API_KEY

def fetch_movies(movie_type, api_key):
    """Fetch movies from TMDB API based on type"""
    if movie_type not in MOVIE_ENDPOINTS:
        raise ValueError(f"Invalid movie type: {movie_type}")
    
    endpoint = MOVIE_ENDPOINTS[movie_type]
    url = f"{TMDB_BASE_URL}{endpoint}"
    
    params = {
        "api_key": api_key,
        "language": "en-US",
        "page": 1
    }
    
    try:
        # Add headers and SSL verification options for better compatibility
        headers = {
            'User-Agent': 'TMDB-CLI-Tool/1.0',
            'Accept': 'application/json'
        }
        
        # Try different connection methods for better compatibility
        session = requests.Session()
        session.headers.update(headers)
        
        # First try with standard SSL verification
        try:
            response = session.get(
                url, 
                params=params, 
                timeout=30,
                verify=True
            )
        except (requests.exceptions.SSLError, requests.exceptions.ConnectionError):
            # If SSL fails, try with more compatible settings
            console.print("[yellow]⚠️  SSL connection failed, trying alternative method...[/yellow]")
            response = session.get(
                url, 
                params=params, 
                timeout=30,
                verify=False  # Disable SSL verification as fallback
            )
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.ConnectionError as e:
        console.print("[red]❌ Connection Error: Unable to connect to TMDB servers.[/red]")
        console.print("[yellow]This could be due to:[/yellow]")
        console.print("  • Network connectivity issues")
        console.print("  • Firewall or proxy blocking the connection")
        console.print("  • TMDB servers temporarily unavailable")
        console.print("[blue]💡 Try again in a few moments or check your internet connection.[/blue]")
        sys.exit(1)
        
    except requests.exceptions.Timeout:
        console.print("[red]⏰ Timeout Error: Request took too long.[/red]")
        console.print("[blue]💡 Please try again. The TMDB servers might be slow.[/blue]")
        sys.exit(1)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            console.print("[red]🔑 Authentication Error: Invalid API key.[/red]")
            console.print("[yellow]Please check your TMDB API key is correct.[/yellow]")
        elif response.status_code == 404:
            console.print("[red]❌ Not Found: The requested endpoint doesn't exist.[/red]")
        else:
            console.print(f"[red]HTTP Error {response.status_code}: {e}[/red]")
        sys.exit(1)
        
    except requests.exceptions.RequestException as e:
        console.print(f"[red]❌ Network Error: {e}[/red]")
        console.print("[yellow]This might be a temporary network issue.[/yellow]")
        console.print("[blue]💡 Please check your internet connection and try again.[/blue]")
        sys.exit(1)

def format_movie_data(movies_data, movie_type):
    """Format movie data for display"""
    movies = movies_data.get("results", [])
    
    if not movies:
        console.print(f"[yellow]No {movie_type} movies found.[/yellow]")
        return
    
    # Create table
    table = Table(
        title=f"{movie_type.title()} Movies",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta"
    )
    
    # Add columns
    table.add_column("Title", style="cyan", width=30)
    table.add_column("Release Date", style="green", width=12)
    table.add_column("Rating", style="yellow", width=8)
    table.add_column("Overview", style="white", width=50)
    
    # Add rows
    for movie in movies[:20]:  # Limit to 20 movies for better display
        title = movie.get("title", "Unknown")
        release_date = movie.get("release_date", "Unknown")
        rating = movie.get("vote_average", 0)
        overview = movie.get("overview", "No overview available")
        
        # Truncate overview if too long
        if len(overview) > 47:
            overview = overview[:47] + "..."
        
        # Format rating
        rating_str = f"{rating:.1f}" if rating else "N/A"
        
        table.add_row(title, release_date, rating_str, overview)
    
    return table

def display_movie_info(movie_type):
    """Display movie information based on type"""
    try:
        api_key = get_api_key()
        
        # Fetch movies
        console.print(f"[blue]Fetching {movie_type} movies...[/blue]")
        movies_data = fetch_movies(movie_type, api_key)
        
        # Format and display data
        table = format_movie_data(movies_data, movie_type)
        if table:
            console.print(table)
            
            # Display additional info
            total_results = movies_data.get("total_results", 0)
            console.print(f"\n[green]Total results: {total_results}[/green]")
            console.print(f"[green]Showing first 20 results[/green]")
        
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        sys.exit(1)

@click.command()
@click.option(
    "--type", 
    "-t",
    "movie_type",
    type=click.Choice(["playing", "popular", "top", "upcoming"]),
    required=True,
    help="Type of movies to fetch (playing, popular, top, upcoming)"
)
def main(movie_type):
    """TMDB CLI Tool - Fetch movie information from The Movie Database"""
    
    # Display welcome message
    welcome_text = Text("🎬 TMDB CLI Tool", style="bold blue")
    welcome_text.append("\nFetching movie information from TMDB...", style="white")
    
    welcome_panel = Panel(
        welcome_text,
        title="Welcome",
        border_style="blue",
        padding=(1, 2)
    )
    
    console.print(welcome_panel)
    console.print()
    
    # Display movie information
    display_movie_info(movie_type)

if __name__ == "__main__":
    main()
