# Towers of Hanoi - Recursive Solution

This project demonstrates how to solve the classic Towers of Hanoi puzzle using recursion in Python.

## Features
- Solves the Towers of Hanoi problem for any number of disks (default: 3).
- Shows the state of all three rods after each move.
- Uses a simple recursive algorithm.

## Files
- `main.py`: Contains the implementation and an example run.

## How it works
The function `move(n, source, auxiliary, target)` recursively moves `n` disks from the source rod to the target rod, using the auxiliary rod as a helper. The state of the rods is printed after each move.

### Example usage
```python
NUMBER_OF_DISKS = 3
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

move(NUMBER_OF_DISKS, A, B, C)
```

## Running the program
To run the program, use:

```bash
python main.py
```

## Example output
```
[3, 2, 1] [] [] 
[3, 2] [] [1] 
[3] [2] [1] 
[3] [2, 1] [] 
[] [2, 1] [3] 
[1] [2] [3] 
[1] [] [3, 2] 
[] [] [3, 2, 1] 
```

## Author
- Course: Scientific Computing with Python
- Part 9: Learn Recursion by Solving the Tower of Hanoi Puzzle