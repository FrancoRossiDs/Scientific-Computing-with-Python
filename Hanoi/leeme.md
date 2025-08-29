# Torres de Hanoi - Solución Recursiva

Este proyecto demuestra cómo resolver el clásico problema de las Torres de Hanoi usando recursividad en Python.

## Características
- Resuelve el problema de las Torres de Hanoi para cualquier cantidad de discos (por defecto: 3).
- Muestra el estado de las tres varillas después de cada movimiento.
- Utiliza un algoritmo recursivo simple.

## Archivos
- `main.py`: Contiene la implementación y un ejemplo de ejecución.

## ¿Cómo funciona?
La función `move(n, source, auxiliary, target)` mueve recursivamente `n` discos desde la varilla origen a la varilla destino, usando la varilla auxiliar como ayuda. El estado de las varillas se imprime después de cada movimiento.

### Ejemplo de uso
```python
NUMBER_OF_DISKS = 3
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

move(NUMBER_OF_DISKS, A, B, C)
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Ejemplo de salida
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

## Autor
- Curso: Scientific Computing with Python
- Parte 9: Learn Recursion by Solving the Tower of Hanoi Puzzle
