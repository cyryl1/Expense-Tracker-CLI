# Expense Tracker

A simple command-line application to manage your personal finances.

## Features

- Add expenses with descriptions and amounts
- Update existing expenses
- Delete expenses
- View all expenses
- View a summary of all expenses
- View a summary of expenses for a specific month (of the current year)

Additional features:
- Expense categories with filtering
- Monthly budget setting with warnings
- Export expenses to CSV

## Installation

[Provide installation instructions here]

## Usage

The application runs from the command line with the following commands:

### Add an expense

```
$ expense-tracker add --description "Lunch" --amount 20
Expense added successfully (ID: 1)
```

### Update an expense

```
$ expense-tracker update --id 1 --description "Business Lunch" --amount 25
Expense updated successfully
```

### Delete an expense

```
$ expense-tracker delete --id 1
Expense deleted successfully
```

### List all expenses

```
$ expense-tracker list
ID  Date       Description  Amount
1   2024-08-06  Lunch        $20
2   2024-08-06  Dinner       $10
```

### View expense summary

```
$ expense-tracker summary
Total expenses: $30
```

### View monthly expense summary

```
$ expense-tracker summary --month 8
Total expenses for August: $20
```

## Implementation Details

- Built with [Python]
- Uses [argparse] for parsing command arguments
- Stores data in a [json] file
- Implements error handling for invalid inputs and edge cases
- Modularized code structure for easy testing and maintenance



