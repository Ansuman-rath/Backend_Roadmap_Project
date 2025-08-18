#!/usr/bin/env python3
"""
Expense Tracker - A simple command-line application to manage personal finances.
"""

import argparse
import json
import csv
import os
from datetime import datetime, date
from typing import Dict, List, Optional
import sys


class ExpenseTracker:
    def __init__(self, data_file: str = "expenses.json"):
        self.data_file = data_file
        self.expenses = self.load_expenses()
        self.next_id = self._get_next_id()
    
    def load_expenses(self) -> List[Dict]:
        """Load expenses from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_expenses(self):
        """Save expenses to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=2, default=str)
    
    def _get_next_id(self) -> int:
        """Get the next available ID for expenses."""
        if not self.expenses:
            return 1
        return max(expense['id'] for expense in self.expenses) + 1
    
    def add_expense(self, description: str, amount: float, category: str = "General") -> int:
        """Add a new expense."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        expense = {
            'id': self.next_id,
            'description': description,
            'amount': amount,
            'category': category,
            'date': date.today().isoformat()
        }
        
        self.expenses.append(expense)
        self.next_id += 1
        self.save_expenses()
        return expense['id']
    
    def update_expense(self, expense_id: int, description: str = None, 
                      amount: float = None, category: str = None) -> bool:
        """Update an existing expense."""
        expense = self.get_expense_by_id(expense_id)
        if not expense:
            return False
        
        if description is not None:
            expense['description'] = description
        if amount is not None:
            if amount <= 0:
                raise ValueError("Amount must be positive")
            expense['amount'] = amount
        if category is not None:
            expense['category'] = category
        
        self.save_expenses()
        return True
    
    def delete_expense(self, expense_id: int) -> bool:
        """Delete an expense by ID."""
        expense = self.get_expense_by_id(expense_id)
        if not expense:
            return False
        
        self.expenses.remove(expense)
        self.save_expenses()
        return True
    
    def get_expense_by_id(self, expense_id: int) -> Optional[Dict]:
        """Get expense by ID."""
        for expense in self.expenses:
            if expense['id'] == expense_id:
                return expense
        return None
    
    def list_expenses(self, category: str = None) -> List[Dict]:
        """List all expenses, optionally filtered by category."""
        if category:
            return [exp for exp in self.expenses if exp['category'].lower() == category.lower()]
        return self.expenses
    
    def get_summary(self, month: int = None) -> Dict:
        """Get summary of expenses, optionally for a specific month."""
        if month is not None:
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12")
            
            current_year = datetime.now().year
            filtered_expenses = [
                exp for exp in self.expenses 
                if datetime.fromisoformat(exp['date']).month == month
                and datetime.fromisoformat(exp['date']).year == current_year
            ]
        else:
            filtered_expenses = self.expenses
        
        total = sum(exp['amount'] for exp in filtered_expenses)
        category_totals = {}
        for exp in filtered_expenses:
            cat = exp['category']
            category_totals[cat] = category_totals.get(cat, 0) + exp['amount']
        
        return {
            'total': total,
            'count': len(filtered_expenses),
            'category_totals': category_totals,
            'month': month
        }
    
    def export_to_csv(self, filename: str = None) -> str:
        """Export expenses to CSV file."""
        if not filename:
            filename = f"expenses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ID', 'Date', 'Description', 'Amount', 'Category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow({
                    'ID': expense['id'],
                    'Date': expense['date'],
                    'Description': expense['description'],
                    'Amount': expense['amount'],
                    'Category': expense['category']
                })
        
        return filename


def format_currency(amount: float) -> str:
    """Format amount as currency."""
    return f"${amount:.2f}"


def display_expenses(expenses: List[Dict]):
    """Display expenses in a formatted table."""
    if not expenses:
        print("No expenses found.")
        return
    
    print(f"{'ID':<4} {'Date':<12} {'Description':<20} {'Amount':<10} {'Category':<15}")
    print("-" * 70)
    
    for expense in expenses:
        print(f"{expense['id']:<4} {expense['date']:<12} "
              f"{expense['description'][:18]:<20} {format_currency(expense['amount']):<10} "
              f"{expense['category'][:13]:<15}")


def display_summary(summary: Dict):
    """Display expense summary."""
    if summary['month']:
        month_name = datetime(2024, summary['month'], 1).strftime('%B')
        print(f"Total expenses for {month_name}: {format_currency(summary['total'])}")
    else:
        print(f"Total expenses: {format_currency(summary['total'])}")
    
    print(f"Number of expenses: {summary['count']}")
    
    if summary['category_totals']:
        print("\nBy category:")
        for category, total in summary['category_totals'].items():
            print(f"  {category}: {format_currency(total)}")


def main():
    parser = argparse.ArgumentParser(
        description="Expense Tracker - Manage your personal finances",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  expense-tracker add --description "Lunch" --amount 20
  expense-tracker add --description "Dinner" --amount 15 --category "Food"
  expense-tracker list
  expense-tracker summary
  expense-tracker summary --month 8
  expense-tracker update --id 1 --amount 25
  expense-tracker delete --id 2
  expense-tracker export
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Expense description')
    add_parser.add_argument('--amount', type=float, required=True, help='Expense amount')
    add_parser.add_argument('--category', default='General', help='Expense category')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update an existing expense')
    update_parser.add_argument('--id', type=int, required=True, help='Expense ID')
    update_parser.add_argument('--description', help='New description')
    update_parser.add_argument('--amount', type=float, help='New amount')
    update_parser.add_argument('--category', help='New category')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', type=int, required=True, help='Expense ID')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all expenses')
    list_parser.add_argument('--category', help='Filter by category')
    
    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Show expense summary')
    summary_parser.add_argument('--month', type=int, help='Month (1-12) for monthly summary')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export expenses to CSV')
    export_parser.add_argument('--filename', help='Output filename (optional)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    tracker = ExpenseTracker()
    
    try:
        if args.command == 'add':
            expense_id = tracker.add_expense(args.description, args.amount, args.category)
            print(f"Expense added successfully (ID: {expense_id})")
        
        elif args.command == 'update':
            if not any([args.description, args.amount, args.category]):
                print("Error: At least one field must be specified for update")
                return
            
            if tracker.update_expense(args.id, args.description, args.amount, args.category):
                print(f"Expense updated successfully (ID: {args.id})")
            else:
                print(f"Error: Expense with ID {args.id} not found")
        
        elif args.command == 'delete':
            if tracker.delete_expense(args.id):
                print(f"Expense deleted successfully (ID: {args.id})")
            else:
                print(f"Error: Expense with ID {args.id} not found")
        
        elif args.command == 'list':
            expenses = tracker.list_expenses(args.category)
            display_expenses(expenses)
        
        elif args.command == 'summary':
            summary = tracker.get_summary(args.month)
            display_summary(summary)
        
        elif args.command == 'export':
            filename = tracker.export_to_csv(args.filename)
            print(f"Expenses exported to {filename}")
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
