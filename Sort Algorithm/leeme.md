# Algoritmo Merge Sort - Mini Proyecto

Este proyecto implementa el algoritmo de ordenamiento Merge Sort en Python para ordenar una lista de números.

## Archivos
- `main.py`: Contiene la implementación del algoritmo merge sort y un ejemplo de uso.

## ¿Cómo funciona?
La función `merge_sort` divide recursivamente la lista en mitades, ordena cada mitad y luego las fusiona en orden. Es un clásico ejemplo de algoritmo divide y vencerás.

### Ejemplo de uso
```python
def merge_sort(array):
    # ...código...

numbers = [4, 10, 6, 14, 2, 1, 8, 5]
print('Unsorted array: ')
print(numbers)
merge_sort(numbers)
print('Sorted array: ' + str(numbers))
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Salida esperada
```
Unsorted array: 
[4, 10, 6, 14, 2, 1, 8, 5]
Sorted array: [1, 2, 4, 5, 6, 8, 10, 14]
```

## Autor
- Franco Rossi
- Parte 10: Learn Data Structures by Building the Merge Sort Algorithm
---
Puedes modificar la lista de números para ordenar diferentes arreglos según lo necesites.
