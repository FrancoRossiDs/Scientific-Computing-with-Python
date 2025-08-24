# Case Converter - Mini Proyecto

Este mini proyecto implementa una función en Python para convertir cadenas en formato PascalCase o camelCase a snake_case.

## Archivos
- `main.py`: Contiene la función para convertir cadenas y un ejemplo de uso.

## ¿Cómo funciona?
La función `convert_to_snake_case` toma una cadena en PascalCase o camelCase y la convierte a snake_case, agregando un guion bajo antes de cada letra mayúscula (excepto la primera) y convirtiendo todas las letras a minúsculas.

### Ejemplo de uso
```python
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')

print(convert_to_snake_case('IAmAPascalCasedString'))  # Salida: i_am_a_pascal_cased_string
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Salida esperada
```
i_am_a_pascal_cased_string
```

## Autor
- Curso: Scientific Computing with Python
- Parte 4: Learn Python List Comprehension by Building a Case Converter Program

---
Puedes modificar la función para soportar otros formatos de conversión si lo deseas.
