# Arithmetic Arranger

This project provides a Python function called `arithmetic_arranger` that formats a list of simple arithmetic problems (addition and subtraction) in the same way elementary students arrange them vertically to make them easier to solve.

## Features
- Arranges arithmetic problems vertically and side by side.
- Supports only addition and subtraction.
- Optionally displays the answers to the problems.
- Returns clear error messages for invalid inputs.

## Usage

Import or use the `arithmetic_arranger` function in your Python code:

```python
from main import arithmetic_arranger

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
```

### Example output
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
With answers:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Rules and validations
- Maximum of five problems per call. If there are more, returns: `Error: Too many problems.`
- Only addition and subtraction are allowed. Other operators return: `Error: Operator must be '+' or '-'.`
- Operands must only contain digits. Otherwise: `Error: Numbers must only contain digits.`
- Operands must be no more than four digits. If not: `Error: Numbers cannot be more than four digits.`
- Problems are formatted with numbers right-aligned, a single space between the operator and operand, and four spaces between each problem.

## File structure
- `main.py`: Contains the function implementation.
- `consigna.md`: Project instructions and requirements.

## Author
- Course: Scientific Computing with Python
- First project: Build an Arithmetic Formatter Project

---
You can try other problems to see the changes.