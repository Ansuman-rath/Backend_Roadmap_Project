# 🎬 TMDB CLI Tool

A command line interface tool to fetch movie information from The Movie Database (TMDB) API. This tool allows you to easily retrieve popular, top-rated, upcoming, and now playing movies directly from your terminal.

[TMDB CLI Tool](https://roadmap.sh/projects/tmdb-cli)

## ✨ Features

- **Multiple Movie Categories**: Fetch different types of movies (playing, popular, top-rated, upcoming)
- **Beautiful Terminal Output**: Rich, formatted tables with color-coded information
- **Error Handling**: Graceful error handling for API failures and network issues
- **Easy to Use**: Simple command line interface with clear options
- **Fast & Efficient**: Optimized API calls with timeout handling

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd tdmi
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your TMDB API key**
   - Visit [TMDB Settings](https://www.themoviedb.org/settings/api)
   - Create a free account if you don't have one
   - Request an API key (v3 auth)
   - Copy your API key

4. **Configure your API key**
   
   **Option 1: Environment variable**
   ```bash
   # Windows (PowerShell)
   $env:TMDB_API_KEY="your_api_key_here"
   
   # Windows (Command Prompt)
   set TMDB_API_KEY=your_api_key_here
   
   # Linux/Mac
   export TMDB_API_KEY="your_api_key_here"
   ```
   
   **Option 2: .env file**
   ```bash
   # Copy the example file
   cp env.example .env
   
   # Edit .env and add your API key
   TMDB_API_KEY=your_actual_api_key_here
   ```

## 📖 Usage

The CLI tool supports four different movie categories:

### Basic Usage

```bash
python tmdb_cli.py --type <movie_type>
```

### Available Movie Types

- **Now Playing Movies**
  ```bash
  python tmdb_cli.py --type playing
  ```

- **Top Rated Movies**
  ```bash
  python tmdb_cli.py --type top
  ```

- **Upcoming Movies**
  ```bash
  python tmdb_cli.py --type upcoming
  ```

### Alternative Syntax

You can also use the short form:
```bash
python tmdb_cli.py -t playing
```

## 📊 Output Format

The tool displays movies in a beautiful, formatted table with the following information:

- **Title**: Movie name
- **Release Date**: When the movie was/will be released
- **Rating**: Average user rating (out of 10)
- **Overview**: Brief description of the movie

## 🔧 Configuration

### Environment Variables

- `TMDB_API_KEY`: Your TMDB API key (required)

### API Endpoints

The tool uses the following TMDB API endpoints:
- Now Playing: `/movie/now_playing`
- Popular: `/movie/popular`
- Top Rated: `/movie/top_rated`
- Upcoming: `/movie/upcoming`

## 🛠️ Error Handling

The tool includes comprehensive error handling for:

- **Missing API Key**: Clear instructions on how to set up the API key
- **Network Issues**: Timeout handling and connection error messages
- **API Failures**: Proper error messages for API-related issues
- **Invalid Input**: Validation of movie type parameters

## 📁 Project Structure

```
tdmi/
├── tmdb_cli.py          # Main CLI application
├── requirements.txt      # Python dependencies
├── env.example          # Example environment configuration
└── README.md           # This file
```

## 🧪 Testing

To test the tool, make sure you have:

1. Set up your TMDB API key
2. Installed all dependencies
3. Internet connection

Then try:
```bash
python tmdb_cli.py --type popular
```

## Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing the free API
- [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- [Click](https://click.palletsprojects.com/) for CLI framework
- [Requests](https://requests.readthedocs.io/) for HTTP library


**Happy movie browsing! 🎭🍿**


