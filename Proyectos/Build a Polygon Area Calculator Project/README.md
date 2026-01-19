# Polygon Area Calculator - Project

This project implements a Python program to calculate area, perimeter, diagonal, and other properties of rectangles and squares using object-oriented programming principles.

## Files
- `main.py`: Contains the Rectangle and Square classes with methods to calculate geometric properties and visualize shapes.

## How does it work?
The project defines two classes:
- **Rectangle**: Represents a rectangle with width and height. Includes methods to:
  - Set and modify dimensions
  - Calculate area, perimeter, and diagonal
  - Generate a visual representation using ASCII characters
  - Determine how many shapes fit inside another shape

- **Square**: Inherits from Rectangle and represents a square where all sides are equal. Ensures that width and height always remain the same.

### Example usage
```python
rect = Rectangle(10, 5)
print(rect.get_area())        # Output: 50
print(rect.get_perimeter())   # Output: 30
print(rect.get_diagonal())    # Output: 11.18...
print(rect.get_picture())     # Displays ASCII art

square = Square(6)
print(square)                 # Output: Square(side=6)
print(square.get_area())      # Output: 36

# How many squares fit in the rectangle?
print(rect.get_amount_inside(square))  # Output: 1
```

## Run
To run the program, use:

```bash
python main.py
```

## Key Methods
- `get_area()`: Returns the area of the shape
- `get_perimeter()`: Returns the perimeter of the shape
- `get_diagonal()`: Returns the length of the diagonal
- `get_picture()`: Returns an ASCII art representation (max 50x50)
- `get_amount_inside(shape)`: Calculates how many of the given shape fit inside
- `set_width()`, `set_height()`: Update dimensions (for Rectangle)
- `set_side()`: Updates side length (for Square)

## Author
- Course: Scientific Computing with Python
- Project: Build a Polygon Area Calculator

---
You can extend this project by adding more shapes (Triangle, Circle, Pentagon) if you wish.
