# Sudoku Solver

This project provides a simple Python implementation for solving Sudoku puzzles using a backtracking algorithm.

## Features
- Solves standard 9x9 Sudoku puzzles.
- Prints the puzzle before and after solving.
- Indicates if a puzzle is unsolvable.

## How It Works
- The `Board` class represents the Sudoku grid and provides methods for checking validity and solving the puzzle.
- The `solve_sudoku` function initializes the board, prints the initial puzzle, attempts to solve it, and prints the result.

## Usage
1. Place your puzzle as a 9x9 list of lists, using `0` for empty cells.
2. Run the script. The solution (if found) will be printed to the console.

### Example
```python
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)
```

## Autor
- Course: Scientific Computing with Python
- Part 10: Learn Classes and Objects by Building a Sudoku Solver

---
You can modify the sudoku to get different results