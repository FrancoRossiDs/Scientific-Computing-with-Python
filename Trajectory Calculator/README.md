# Trajectory Calculator - Project

This project implements a Python program to calculate and visualize the trajectory of a projectile using physics equations and object-oriented programming.

## Files
- `main.py`: Contains the Projectile and Graph classes to calculate projectile motion, generate coordinate tables, and create ASCII art visualizations.

## How does it work?
The project defines two main classes:
- **Projectile**: Represents a projectile with initial speed, height, and launch angle. Calculates:
  - Horizontal displacement
  - All coordinates (x, y) along the trajectory
  - Applies gravitational acceleration (9.81 m/s²)
  - Uses physics formulas for projectile motion

- **Graph**: Takes projectile coordinates and:
  - Creates a table showing all x, y coordinates
  - Generates an ASCII art visualization of the trajectory
  - Uses special characters (∙, T, ⊣) for display

### Example usage
```python
from main import projectile_helper

# Launch a projectile with 10 m/s speed, 3 m initial height, 45° angle
projectile_helper(10, 3, 45)
```

## Run
To run the program, use:

```bash
python main.py
```

## Expected output
```
Projectile details:
speed: 10 m/s
height: 3 m
angle: 45°
displacement: 12.2 m

  x      y
  0   3.00
  1   3.91
  2   4.73
  3   5.46
...

⊣                    ∙
⊣                  ∙
⊣                ∙
⊣              ∙
⊣            ∙
⊣        ∙
⊣    ∙
⊣  ∙
⊣∙
 T∙∙∙∙∙∙∙∙∙∙∙
```

## Key Features
- Calculates complete projectile trajectories
- Displays coordinates in table format
- Creates ASCII art visualization of the path
- Uses private attributes with `__slots__` for memory efficiency
- Implements properties with getters and setters
- Applies realistic gravitational physics

## Author
- Course: Scientific Computing with Python
- Part 14: Learn Encapsulation by Building a Projectile Trajectory Calculator

---
You can modify the initial parameters (speed, height, angle) to simulate different projectile scenarios if you wish.
