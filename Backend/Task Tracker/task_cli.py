#!/usr/bin/env python3
"""
Task Tracker CLI - A simple command line interface to track and manage tasks.
"""

import json
import sys
import os
from datetime import datetime
from typing import Dict, List, Optional


class TaskTracker:
    """Main class for managing tasks and CLI operations."""
    
    def __init__(self, data_file: str = "tasks.json"):
        """Initialize the TaskTracker with a JSON file for data storage."""
        self.data_file = data_file
        self.tasks = self._load_tasks()
    
    def _load_tasks(self) -> Dict[str, List[Dict]]:
        """Load tasks from JSON file or create empty structure if file doesn't exist."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            else:
                # Create empty task structure
                return {"tasks": []}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
            return {"tasks": []}
    
    def _save_tasks(self) -> bool:
        """Save tasks to JSON file."""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, indent=2, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def _get_next_id(self) -> int:
        """Get the next available task ID."""
        if not self.tasks["tasks"]:
            return 1
        return max(task["id"] for task in self.tasks["tasks"]) + 1
    
    def _find_task_by_id(self, task_id: int) -> Optional[Dict]:
        """Find a task by its ID."""
        for task in self.tasks["tasks"]:
            if task["id"] == task_id:
                return task
        return None
    
    def add_task(self, description: str) -> bool:
        """Add a new task."""
        if not description.strip():
            print("Error: Task description cannot be empty.")
            return False
        
        task = {
            "id": self._get_next_id(),
            "description": description.strip(),
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        
        self.tasks["tasks"].append(task)
        
        if self._save_tasks():
            print(f"Task added successfully (ID: {task['id']})")
            return True
        else:
            print("Error: Failed to save task.")
            return False
    
    def update_task(self, task_id: int, new_description: str) -> bool:
        """Update an existing task's description."""
        if not new_description.strip():
            print("Error: Task description cannot be empty.")
            return False
        
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return False
        
        task["description"] = new_description.strip()
        task["updatedAt"] = datetime.now().isoformat()
        
        if self._save_tasks():
            print(f"Task {task_id} updated successfully.")
            return True
        else:
            print("Error: Failed to save updated task.")
            return False
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return False
        
        self.tasks["tasks"].remove(task)
        
        if self._save_tasks():
            print(f"Task {task_id} deleted successfully.")
            return True
        else:
            print("Error: Failed to save after deletion.")
            return False
    
    def mark_task_status(self, task_id: int, status: str) -> bool:
        """Mark a task as in-progress or done."""
        valid_statuses = ["todo", "in-progress", "done"]
        if status not in valid_statuses:
            print(f"Error: Invalid status. Must be one of: {', '.join(valid_statuses)}")
            return False
        
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return False
        
        old_status = task["status"]
        task["status"] = status
        task["updatedAt"] = datetime.now().isoformat()
        
        if self._save_tasks():
            print(f"Task {task_id} marked as {status} (was: {old_status}).")
            return True
        else:
            print("Error: Failed to save task status.")
            return False
    
    def list_tasks(self, status_filter: Optional[str] = None) -> None:
        """List all tasks or tasks filtered by status."""
        if not self.tasks["tasks"]:
            print("No tasks found.")
            return
        
        filtered_tasks = self.tasks["tasks"]
        if status_filter:
            valid_statuses = ["todo", "in-progress", "done"]
            if status_filter not in valid_statuses:
                print(f"Error: Invalid status filter. Must be one of: {', '.join(valid_statuses)}")
                return
            filtered_tasks = [task for task in self.tasks["tasks"] if task["status"] == status_filter]
            
            if not filtered_tasks:
                print(f"No tasks found with status: {status_filter}")
                return
        
        print(f"\n{'ID':<4} {'Status':<12} {'Description':<50} {'Created':<20} {'Updated':<20}")
        print("-" * 110)
        
        for task in filtered_tasks:
            created = datetime.fromisoformat(task["createdAt"]).strftime("%Y-%m-%d %H:%M")
            updated = datetime.fromisoformat(task["updatedAt"]).strftime("%Y-%m-%d %H:%M")
            description = task["description"][:47] + "..." if len(task["description"]) > 47 else task["description"]
            
            print(f"{task['id']:<4} {task['status']:<12} {description:<50} {created:<20} {updated:<20}")
        
        print(f"\nTotal tasks: {len(filtered_tasks)}")


def print_usage():
    """Print usage information."""
    print("""
Task Tracker CLI - Manage your tasks from the command line

Usage:
  python task_cli.py <command> [arguments]

Commands:
  add <description>           Add a new task
  update <id> <description>  Update an existing task
  delete <id>                Delete a task
  mark-in-progress <id>      Mark a task as in progress
  mark-done <id>             Mark a task as done
  list [status]              List all tasks or tasks by status
  help                       Show this help message

Status values:
  todo, in-progress, done

Examples:
  python task_cli.py add "Buy groceries"
  python task_cli.py update 1 "Buy groceries and cook dinner"
  python task_cli.py mark-done 1
  python task_cli.py list
  python task_cli.py list done
""")


def main():
    """Main function to handle CLI arguments and execute commands."""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1].lower()
    tracker = TaskTracker()
    
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Task description is required.")
                print("Usage: python task_cli.py add <description>")
                return
            description = " ".join(sys.argv[2:])
            tracker.add_task(description)
        
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Task ID and new description are required.")
                print("Usage: python task_cli.py update <id> <description>")
                return
            try:
                task_id = int(sys.argv[2])
                new_description = " ".join(sys.argv[3:])
                tracker.update_task(task_id, new_description)
            except ValueError:
                print("Error: Task ID must be a number.")
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Task ID is required.")
                print("Usage: python task_cli.py delete <id>")
                return
            try:
                task_id = int(sys.argv[2])
                tracker.delete_task(task_id)
            except ValueError:
                print("Error: Task ID must be a number.")
        
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Task ID is required.")
                print("Usage: python task_cli.py mark-in-progress <id>")
                return
            try:
                task_id = int(sys.argv[2])
                tracker.mark_task_status(task_id, "in-progress")
            except ValueError:
                print("Error: Task ID must be a number.")
        
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Task ID is required.")
                print("Usage: python task_cli.py mark-done <id>")
                return
            try:
                task_id = int(sys.argv[2])
                tracker.mark_task_status(task_id, "done")
            except ValueError:
                print("Error: Task ID must be a number.")
        
        elif command == "list":
            status_filter = sys.argv[2] if len(sys.argv) > 2 else None
            tracker.list_tasks(status_filter)
        
        elif command in ["help", "--help", "-h"]:
            print_usage()
        
        else:
            print(f"Error: Unknown command '{command}'")
            print_usage()
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
