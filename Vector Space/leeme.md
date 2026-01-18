# Clase R2Vector - Vectores en 2D

Este mini proyecto implementa una clase `R2Vector` en Python para representar y operar con vectores en un espacio bidimensional.

## Archivos
- `main.py`: Contiene la implementación de la clase R2Vector con sus operaciones.

## ¿Cómo funciona?
La clase R2Vector permite al usuario:
- Crear vectores bidimensionales con coordenadas x e y.
- Calcular la norma (magnitud) de un vector.
- Realizar operaciones de suma entre vectores.
- Realizar operaciones de resta entre vectores.
- Multiplicar vectores por escalares.
- Calcular el producto punto entre dos vectores.
- Comparar vectores por igualdad y por norma.

Implementa métodos especiales de Python (dunder methods) para permitir operaciones intuitivas con los vectores.

### Ejemplo de uso
```python
# Crear vectores
v1 = R2Vector(x=3, y=4)
v2 = R2Vector(x=1, y=2)

# Calcular norma
print(v1.norm())  # 5.0

# Suma de vectores
v3 = v1 + v2  # R2Vector(x=4, y=6)

# Resta de vectores
v4 = v1 - v2  # R2Vector(x=2, y=2)

# Multiplicar por escalar
v5 = v1 * 2  # R2Vector(x=6, y=8)

# Producto punto
producto = v1 * v2  # 11
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Características de la clase
- **`__init__(*, x, y)`**: Constructor que requiere argumentos nombrados.
- **`norm()`**: Calcula la norma euclidiana del vector.
- **`__str__()`**: Representación en formato tupla.
- **`__repr__()`**: Representación técnica de la clase.
- **`__add__()`**: Suma de vectores.
- **`__sub__()`**: Resta de vectores.
- **`__mul__()`**: Multiplicación por escalar o producto punto.
- **`__eq__()` y `__ne__()`**: Comparación de igualdad.
- **`__lt__()`**: Comparación por norma (magnitud).

## Autor
- Curso: Scientific Computing with Python
- Parte 12: Learn Special Methods by Building a Vector Space
