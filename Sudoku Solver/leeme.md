# Solucionador de Sudoku

Este proyecto proporciona una implementación sencilla en Python para resolver sudokus utilizando un algoritmo de backtracking.

## Características
- Resuelve sudokus estándar de 9x9.
- Imprime el tablero antes y después de resolverlo.
- Indica si el sudoku no tiene solución.

## Cómo funciona
- La clase `Board` representa la cuadrícula del sudoku y ofrece métodos para verificar la validez y resolver el tablero.
- La función `solve_sudoku` inicializa el tablero, imprime el sudoku inicial, intenta resolverlo e imprime el resultado.

## Uso
1. Coloca tu sudoku como una lista de listas de 9x9, usando `0` para las casillas vacías.
2. Ejecuta el script. La solución (si existe) se mostrará en la consola.

### Ejemplo
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
- Curso: Scientific Computing with Python
- Parte 10: Learn Classes and Objects by Building a Sudoku Solver

---
Puedes modificar el sudoku para obtener diferentes resultados