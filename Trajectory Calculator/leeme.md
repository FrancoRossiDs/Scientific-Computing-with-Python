# Trajectory Calculator - Proyecto

Este proyecto implementa un programa en Python para calcular y visualizar la trayectoria de un proyectil utilizando ecuaciones de física y programación orientada a objetos.

## Archivos
- `main.py`: Contiene las clases Projectile y Graph para calcular el movimiento del proyectil, generar tablas de coordenadas y crear visualizaciones en arte ASCII.

## ¿Cómo funciona?
El proyecto define dos clases principales:
- **Projectile**: Representa un proyectil con velocidad inicial, altura y ángulo de lanzamiento. Calcula:
  - Desplazamiento horizontal
  - Todas las coordenadas (x, y) a lo largo de la trayectoria
  - Aplica aceleración gravitatoria (9.81 m/s²)
  - Utiliza fórmulas de física para movimiento de proyectiles

- **Graph**: Toma las coordenadas del proyectil y:
  - Crea una tabla mostrando todas las coordenadas x, y
  - Genera una visualización en arte ASCII de la trayectoria
  - Utiliza caracteres especiales (∙, T, ⊣) para la visualización

### Ejemplo de uso
```python
from main import projectile_helper

# Lanza un proyectil con velocidad 10 m/s, altura inicial 3 m, ángulo 45°
projectile_helper(10, 3, 45)
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Salida esperada
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

## Características Principales
- Calcula trayectorias completas de proyectiles
- Muestra coordenadas en formato de tabla
- Crea visualización en arte ASCII del camino
- Utiliza atributos privados con `__slots__` para eficiencia de memoria
- Implementa propiedades con getters y setters
- Aplica física gravitatoria realista

## Autor
- Curso: Scientific Computing with Python
- Part 14: Learn Encapsulation by Building a Projectile Trajectory Calculator

---
Puedes modificar los parámetros iniciales (velocidad, altura, ángulo) para simular diferentes escenarios de proyectiles si lo deseas.
