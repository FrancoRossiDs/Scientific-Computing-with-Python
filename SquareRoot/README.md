# Square Root Bisection - Mini Project

This mini project implements an algorithm to calculate the square root of a number using the bisection method in Python.

## Files
- `main.py`: Contains the function to calculate the square root and an example of usage.

## How does it work?
The function `square_root_bisection` calculates the square root of a positive number using the bisection method, which is an iterative numerical method. You can specify the tolerance and the maximum number of iterations.

### Example usage
```python
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # ...code...

N = 16
square_root_bisection(N)  # Output: The square root of 16 is approximately 4.0
```

## Run
To run the program, use:

```bash
python main.py
```

## Expected output
```
The square root of 16 is approximately 4.0
```

## Author
- Course: Scientific Computing with Python
- Part 5: Learn the Bisection Method by Finding the Square Root of a Number

---
You can modify the tolerance and number of iterations to experiment with the result's precision.