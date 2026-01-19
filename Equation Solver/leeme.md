# Equation Solver - Ecuaciones lineales y cuadráticas

Este mini proyecto implementa un resolvedor de ecuaciones lineales y cuadráticas en Python usando clases, herencia y métodos abstractos para encapsular la lógica de cada tipo de ecuación.

## Archivos
- `main.py`: Contiene las clases `Equation`, `LinearEquation`, `QuadraticEquation` y la función `solver` para obtener soluciones y análisis.

## ¿Cómo funciona?
La jerarquía define una clase base abstracta `Equation` que valida coeficientes y formatea la ecuación. Las subclases implementan:
- `LinearEquation`: Calcula la pendiente, el intercepto y la solución única.
- `QuadraticEquation`: Calcula el discriminante, las raíces reales (si existen) y analiza vértice y concavidad.

La función `solver()` recibe una instancia de `Equation`, llama `solve()` y `analyze()`, y devuelve un reporte con soluciones y detalles formateados.

### Ejemplo de uso
```python
lin_eq = LinearEquation(2, 3)
quad_eq = QuadraticEquation(1, 2, 1)

print(solver(lin_eq))
print(solver(quad_eq))
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Ejemplo de salida
```
----Linear Equation-----

        2x +3 = 0       

-------Solutions--------

        x = -1.500      

--------Details---------

slope =           2.000
y-intercept =     3.000
```

## Autor
- Curso: Scientific Computing with Python
- Parte 13: Learn Interfaces by Building an Equation Solver
