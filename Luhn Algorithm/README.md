# Luhn Algorithm Mini Proyecto

Este proyecto implementa el algoritmo de Luhn en Python para verificar la validez de números de tarjetas de crédito.

## Archivos
- `main.py`: Contiene la lógica para validar un número de tarjeta usando el algoritmo de Luhn.

## ¿Cómo funciona?
El programa toma un número de tarjeta (puede contener guiones o espacios), lo limpia y verifica si es válido según el algoritmo de Luhn.

### Ejemplo de uso
```python
def verify_card_number(card_number):
    # ...código...

card_number = '4111-1111-4555-1142'
card_translation = str.maketrans({'-': '', ' ': ''})
translated_card_number = card_number.translate(card_translation)

if verify_card_number(translated_card_number):
    print('VALID!')
else:
    print('INVALID!')
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Salida esperada
```
VALID!
```

## Autor
- Curso: Scientific Computing with Python
- Parte 2: Learn How to Work with Numbers and Strings by Implementing the Luhn Algorithm

---
Puedes probar con otros números de tarjeta para ver si son válidos o no.
