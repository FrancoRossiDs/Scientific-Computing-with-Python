# Lambda Function - Expense Tracker

This mini project is a simple expense tracker in Python that uses lambda functions and functional programming to manage and analyze expenses.

## Files
- `main.py`: Contains the logic to add, list, filter, and sum expenses using lambda functions.

## How does it work?
The program allows the user to:
- Add an expense with amount and category.
- List all entered expenses.
- Calculate the total expenses.
- Filter expenses by category.

It uses lambda functions to efficiently sum and filter expenses.

### Example usage
```python
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
```

## Run
To run the program, use:

```bash
python main.py
```

## Example interaction
```
Expense Tracker
1. Add an expense
2. List all expenses
...
```

## Author
- Course: Scientific Computing with Python
- Part 3: Learn Lambda Functions by Building an Expense Tracker
