#!/usr/bin/env python3
"""
Test demonstration script for Task Tracker CLI.
This script demonstrates the basic functionality of the task tracker.
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a CLI command and return the result."""
    try:
        result = subprocess.run(
            [sys.executable, "task_cli.py"] + command.split(),
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def demo():
    """Run a demonstration of the Task Tracker CLI."""
    print("🚀 Task Tracker CLI Demonstration")
    print("=" * 50)
    
    # Clear any existing tasks
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
        print("Cleared existing tasks.json file")
    
    print("\n1. Adding sample tasks...")
    print("-" * 30)
    
    # Add some sample tasks
    print(run_command('add "Learn Python CLI development"'))
    print(run_command('add "Buy groceries for dinner"'))
    print(run_command('add "Complete project documentation"'))
    print(run_command('add "Schedule dentist appointment"'))
    
    print("\n2. Listing all tasks...")
    print("-" * 30)
    print(run_command('list'))
    
    print("\n3. Marking tasks as in-progress...")
    print("-" * 30)
    print(run_command('mark-in-progress 1'))
    print(run_command('mark-in-progress 3'))
    
    print("\n4. Marking a task as done...")
    print("-" * 30)
    print(run_command('mark-done 2'))
    
    print("\n5. Updating a task...")
    print("-" * 30)
    print(run_command('update 4 "Schedule dentist appointment for next week"'))
    
    print("\n6. Listing tasks by status...")
    print("-" * 30)
    print("Todo tasks:")
    print(run_command('list todo'))
    
    print("\nIn-progress tasks:")
    print(run_command('list in-progress'))
    
    print("\nDone tasks:")
    print(run_command('list done'))
    
    print("\n7. Final task list...")
    print("-" * 30)
    print(run_command('list'))
    
    print("\n8. Deleting a task...")
    print("-" * 30)
    print(run_command('delete 1'))
    
    print("\n9. Final state after deletion...")
    print("-" * 30)
    print(run_command('list'))
    
    print("\n✅ Demonstration completed!")
    print("\nYou can now try the CLI yourself:")
    print("  python task_cli.py help")
    print("  python task_cli.py add 'Your task here'")
    print("  python task_cli.py list")

if __name__ == "__main__":
    demo()
