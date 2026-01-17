# Build a Budget App Project

This project implements a budget application in Python that manages different budget categories with a ledger system, allowing deposits, withdrawals, transfers, and a visual representation of spending percentages.

## Files
- `main.py`: Contains the implementation of the Category class and the create_spend_chart function.

## How does it work?
The `Category` class represents a budget category and maintains a ledger of transactions. It supports:
- **deposit**: Add money to a category with an optional description
- **withdraw**: Remove money from a category if funds are available
- **get_balance**: Retrieve the current balance
- **transfer**: Transfer money between categories
- **check_funds**: Verify if sufficient funds are available
- **__str__**: Display the category ledger in a formatted table

The `create_spend_chart` function generates a visual bar chart showing the percentage of total spending for each category.

### Example usage
```python
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```

## Running the program
To run the program, use:

```bash
python main.py
```

## Expected output
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

## Author
- Franco Rossi
- Third Project: Build a Budget App Project
---
You can modify the input values and categories to test different scenarios.
