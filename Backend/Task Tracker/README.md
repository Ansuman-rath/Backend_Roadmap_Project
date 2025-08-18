# Task Tracker CLI

A simple command line interface (CLI) application to track and manage your tasks and to-do lists. Built with Python using only native libraries - no external dependencies required.

[Task Tracker CLI](https://roadmap.sh/projects/task-tracker)

## Features

- ✅ **Add tasks** - Create new tasks with descriptions
- ✅ **Update tasks** - Modify existing task descriptions
- ✅ **Delete tasks** - Remove tasks by ID
- ✅ **Status management** - Mark tasks as todo, in-progress, or done
- ✅ **List tasks** - View all tasks or filter by status
- ✅ **Persistent storage** - Tasks are saved to a JSON file
- ✅ **Error handling** - Graceful error handling for edge cases
- ✅ **Cross-platform** - Works on Windows, macOS, and Linux

## Requirements

- Python 3.6 or higher
- No external libraries or frameworks required

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Ensure Python is installed and accessible from command line

## Usage

### Basic Commands

```bash
# Add a new task
python task_cli.py add "Buy groceries"

# Update an existing task
python task_cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli.py delete 1

# Mark a task as in progress
python task_cli.py mark-in-progress 1

# Mark a task as done
python task_cli.py mark-done 1

# List all tasks
python task_cli.py list

# List tasks by status
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress

# Show help
python task_cli.py help
```

### Command Reference

| Command | Arguments | Description |
|---------|-----------|-------------|
| `add` | `<description>` | Add a new task |
| `update` | `<id> <description>` | Update an existing task |
| `delete` | `<id>` | Delete a task by ID |
| `mark-in-progress` | `<id>` | Mark a task as in progress |
| `mark-done` | `<id>` | Mark a task as done |
| `list` | `[status]` | List all tasks or filter by status |
| `help` | None | Show usage information |

### Status Values

- `todo` - Task is pending
- `in-progress` - Task is currently being worked on
- `done` - Task is completed

## Task Properties

Each task contains the following properties:

- **id**: Unique identifier (auto-generated)
- **description**: Task description text
- **status**: Current status (todo/in-progress/done)
- **createdAt**: Timestamp when task was created
- **updatedAt**: Timestamp when task was last modified

## Data Storage

Tasks are automatically saved to a `tasks.json` file in the current directory. The file is created automatically when you add your first task.

Example `tasks.json` structure:
```json
{
  "tasks": [
    {
      "id": 1,
      "description": "Buy groceries",
      "status": "todo",
      "createdAt": "2024-01-15T10:30:00",
      "updatedAt": "2024-01-15T10:30:00"
    }
  ]
}
```

## Examples

### Workflow Example

```bash
# Create a shopping list
python task_cli.py add "Buy milk"
python task_cli.py add "Get bread"
python task_cli.py add "Pick up dry cleaning"

# View all tasks
python task_cli.py list

# Start shopping
python task_cli.py mark-in-progress 1

# Complete items
python task_cli.py mark-done 1
python task_cli.py mark-done 2

# View what's left
python task_cli.py list todo
```

## Error Handling

The application handles various error cases gracefully:

- Invalid task IDs
- Missing required arguments
- File I/O errors
- Invalid status values
- Empty task descriptions
