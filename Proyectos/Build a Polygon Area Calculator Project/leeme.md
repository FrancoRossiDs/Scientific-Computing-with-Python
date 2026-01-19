# Polygon Area Calculator - Proyecto

Este proyecto implementa un programa en Python para calcular el área, perímetro, diagonal y otras propiedades de rectángulos y cuadrados utilizando principios de programación orientada a objetos.

## Archivos
- `main.py`: Contiene las clases Rectangle y Square con métodos para calcular propiedades geométricas y visualizar formas.

## ¿Cómo funciona?
El proyecto define dos clases:
- **Rectangle**: Representa un rectángulo con ancho y alto. Incluye métodos para:
  - Establecer y modificar dimensiones
  - Calcular área, perímetro y diagonal
  - Generar una representación visual usando caracteres ASCII
  - Determinar cuántas formas caben dentro de otra forma

- **Square**: Hereda de Rectangle y representa un cuadrado donde todos los lados son iguales. Asegura que el ancho y alto siempre sean los mismos.

### Ejemplo de uso
```python
rect = Rectangle(10, 5)
print(rect.get_area())        # Salida: 50
print(rect.get_perimeter())   # Salida: 30
print(rect.get_diagonal())    # Salida: 11.18...
print(rect.get_picture())     # Muestra arte ASCII

square = Square(6)
print(square)                 # Salida: Square(side=6)
print(square.get_area())      # Salida: 36

# ¿Cuántos cuadrados caben en el rectángulo?
print(rect.get_amount_inside(square))  # Salida: 1
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Métodos Principales
- `get_area()`: Devuelve el área de la forma
- `get_perimeter()`: Devuelve el perímetro de la forma
- `get_diagonal()`: Devuelve la longitud de la diagonal
- `get_picture()`: Devuelve una representación en arte ASCII (máx. 50x50)
- `get_amount_inside(shape)`: Calcula cuántas de las formas dadas caben dentro
- `set_width()`, `set_height()`: Actualizar dimensiones (para Rectangle)
- `set_side()`: Actualizar la longitud del lado (para Square)

## Autor
- Curso: Scientific Computing with Python
- Proyecto: Build a Polygon Area Calculator

---
Puedes extender este proyecto agregando más formas (Triángulo, Círculo, Pentágono) si lo deseas.
