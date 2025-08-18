# Expense Tracker

A simple command-line application to manage your personal finances. Track your expenses, categorize them, and get insights into your spending patterns.

[Expense Tracker](https://roadmap.sh/projects/expense-tracker)

## Features

- ✅ **Add expenses** with description, amount, and category
- ✅ **Update existing expenses** (description, amount, category)
- ✅ **Delete expenses** by ID
- ✅ **List all expenses** with optional category filtering
- ✅ **View expense summaries** (total, count, by category)
- ✅ **Monthly summaries** for specific months
- ✅ **Export to CSV** for backup and analysis
- ✅ **Persistent storage** using JSON files
- ✅ **Error handling** for invalid inputs and edge cases

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download this repository
2. Ensure Python 3.6+ is installed on your system
3. No additional packages need to be installed

## Usage

### Basic Commands

#### Add an Expense
```bash
python expense_tracker.py add --description "Lunch" --amount 20
python expense_tracker.py add --description "Dinner" --amount 15 --category "Food"
```

#### List All Expenses
```bash
python expense_tracker.py list
python expense_tracker.py list --category "Food"
```

#### View Summary
```bash
python expense_tracker.py summary                    # Total summary
python expense_tracker.py summary --month 8          # August summary
```

#### Update an Expense
```bash
python expense_tracker.py update --id 1 --amount 25
python expense_tracker.py update --id 1 --description "Lunch with colleagues"
```

#### Delete an Expense
```bash
python expense_tracker.py delete --id 2
```

#### Export to CSV
```bash
python expense_tracker.py export                     # Auto-generated filename
python expense_tracker.py export --filename "my_expenses.csv"
```

### Example Session

```bash
$ python expense_tracker.py add --description "Lunch" --amount 20
Expense added successfully (ID: 1)

$ python expense_tracker.py add --description "Dinner" --amount 10
Expense added successfully (ID: 2)

$ python expense_tracker.py list
ID  Date       Description  Amount     Category
----------------------------------------------------------------------
1   2024-08-06  Lunch        $20.00     General
2   2024-08-06  Dinner       $10.00     General

$ python expense_tracker.py summary
Total expenses: $30.00
Number of expenses: 2

By category:
  General: $30.00

$ python expense_tracker.py delete --id 2
Expense deleted successfully

$ python expense_tracker.py summary
Total expenses: $20.00
Number of expenses: 1

By category:
  General: $20.00
```

## Data Storage

Expenses are stored in a JSON file (`expenses.json`) in the same directory as the script. The file is automatically created when you add your first expense.

## Error Handling

The application includes comprehensive error handling for:
- Invalid amounts (negative or zero)
- Non-existent expense IDs
- Invalid month numbers
- File I/O errors
- JSON parsing errors

## Advanced Features

### Categories
- Default category is "General"
- Categories are case-insensitive when filtering
- You can assign any category name you want

### Monthly Summaries
- Use `--month` with numbers 1-12 (January = 1, December = 12)
- Only shows expenses from the current year
- Useful for monthly budgeting

### CSV Export
- Automatically generates timestamped filenames
- Includes all expense fields
- Compatible with Excel, Google Sheets, and other spreadsheet applications

