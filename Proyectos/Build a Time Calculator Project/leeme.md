# Proyecto Calculadora de Tiempo

Este proyecto implementa una calculadora de tiempo en Python que suma una duración a una hora inicial y devuelve la hora resultante, incluyendo opcionalmente el día de la semana.

## Archivos
- `main.py`: Contiene la implementación de la calculadora de tiempo y un ejemplo de uso.

## ¿Cómo funciona?
La función `add_time` recibe una hora inicial (en formato de 12 horas con AM/PM), una duración (en horas y minutos) y, opcionalmente, un día de la semana. Calcula la nueva hora, ajusta el AM/PM y puede devolver el nuevo día si se proporciona. También indica si el resultado es el día siguiente o varios días después.

### Ejemplo de uso
```python
def add_time(start_time, duration_time, starting_day=''):
    # ...código...

print(add_time('3:00 PM', '3:10'))  # Salida: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Salida: 2:02 PM, Monday
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Salida esperada
```
6:10 PM
```

## Autor
- Franco Rossi
- Segundo proyecto: Build a Time Calculator Project
---
Puedes modificar los valores de entrada para probar diferentes escenarios y días.
