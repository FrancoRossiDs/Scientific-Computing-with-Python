# Square Root Bisection - Mini Proyecto

Este mini proyecto implementa un algoritmo para calcular la raíz cuadrada de un número usando el método de bisección en Python.

## Archivos
- `main.py`: Contiene la función para calcular la raíz cuadrada y un ejemplo de uso.

## ¿Cómo funciona?
La función `square_root_bisection` calcula la raíz cuadrada de un número positivo usando el método de bisección, que es un método numérico iterativo. Permite especificar la tolerancia y el número máximo de iteraciones.

### Ejemplo de uso
```python
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # ...código...

N = 16
square_root_bisection(N)  # Salida: The square root of 16 is approximately 4.0
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Salida esperada
```
The square root of 16 is approximately 4.0
```

## Autor
- Curso: Scientific Computing with Python
- Parte 5: Learn the Bisection Method by Finding the Square Root of a Number

---
Puedes modificar los parámetros de tolerancia y número de iteraciones para experimentar con la precisión del resultado.
