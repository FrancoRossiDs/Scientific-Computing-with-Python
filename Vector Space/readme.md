# R2Vector Class - 2D Vectors

This mini project implements an `R2Vector` class in Python to represent and operate with vectors in a two-dimensional space.

## Files
- `main.py`: Contains the implementation of the R2Vector class with its operations.

## How does it work?
The R2Vector class allows the user to:
- Create two-dimensional vectors with x and y coordinates.
- Calculate the norm (magnitude) of a vector.
- Perform vector addition operations.
- Perform vector subtraction operations.
- Multiply vectors by scalars.
- Calculate the dot product between two vectors.
- Compare vectors by equality and by norm.

It implements special Python methods (dunder methods) to enable intuitive operations with vectors.

### Example usage
```python
# Create vectors
v1 = R2Vector(x=3, y=4)
v2 = R2Vector(x=1, y=2)

# Calculate norm
print(v1.norm())  # 5.0

# Vector addition
v3 = v1 + v2  # R2Vector(x=4, y=6)

# Vector subtraction
v4 = v1 - v2  # R2Vector(x=2, y=2)

# Multiply by scalar
v5 = v1 * 2  # R2Vector(x=6, y=8)

# Dot product
producto = v1 * v2  # 11
```

## Run
To run the program, use:

```bash
python main.py
```

## Class Features
- **`__init__(*, x, y)`**: Constructor that requires named arguments.
- **`norm()`**: Calculates the Euclidean norm of the vector.
- **`__str__()`**: Representation in tuple format.
- **`__repr__()`**: Technical representation of the class.
- **`__add__()`**: Vector addition.
- **`__sub__()`**: Vector subtraction.
- **`__mul__()`**: Scalar multiplication or dot product.
- **`__eq__()` and `__ne__()`**: Equality comparison.
- **`__lt__()`**: Comparison by norm (magnitude).

## Author
- Course: Scientific Computing with Python
- Part 12: Learn Special Methods by Building a Vector Space