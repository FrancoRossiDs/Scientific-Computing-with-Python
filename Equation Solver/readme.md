# Equation Solver - Linear and Quadratic Equations

This mini project implements a solver for linear and quadratic equations in Python, using classes, inheritance, and abstract methods to encapsulate the logic for each equation type.

## Files
- `main.py`: Contains the `Equation`, `LinearEquation`, `QuadraticEquation` classes, and the `solver` function to produce solutions and analysis.

## How does it work?
The hierarchy defines an abstract base class `Equation` that validates coefficients and formats the equation. Subclasses implement:
- `LinearEquation`: Computes slope, intercept, and the single solution.
- `QuadraticEquation`: Computes the discriminant, real roots (if any), and analyzes vertex and concavity.

The `solver()` function takes an `Equation` instance, calls `solve()` and `analyze()`, and returns a formatted report with solutions and details.

### Example usage
```python
lin_eq = LinearEquation(2, 3)
quad_eq = QuadraticEquation(1, 2, 1)

print(solver(lin_eq))
print(solver(quad_eq))
```

## Run
To run the program, use:

```bash
python main.py
```

## Example output
```
----Linear Equation-----

        2x +3 = 0       

-------Solutions--------

        x = -1.500      

--------Details---------

slope =           2.000
y-intercept =     3.000
```

## Author
- Course: Scientific Computing with Python
- Part 13: Learn Interfaces by Building an Equation Solver
