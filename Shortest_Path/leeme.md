# Camino Más Corto - Ejemplo de Algoritmo de Dijkstra

Este proyecto demuestra cómo encontrar el camino más corto en un grafo no dirigido y ponderado usando una implementación simple del algoritmo de Dijkstra en Python.

## Características
- Calcula la distancia más corta desde un nodo inicial a todos los demás nodos del grafo.
- Imprime el camino más corto y la distancia para cada nodo.
- El grafo se representa como una lista de adyacencia con pesos.
- Fácilmente adaptable a diferentes grafos y nodos de inicio.

## Archivos
- `main.py`: Contiene la definición del grafo, la función de camino más corto y un ejemplo de uso.

## ¿Cómo funciona?
La función `shortest_path(graph, start, target='')` calcula los caminos más cortos desde el nodo `start` a todos los demás nodos (o a un nodo `target` específico si se proporciona) usando un enfoque similar a Dijkstra. Imprime la distancia y el camino para cada nodo.

### Ejemplo de uso
```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

shortest_path(my_graph, 'A')
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Ejemplo de salida
```
A-B distance: 5
Path: A -> B

A-C distance: 3
Path: A -> C

A-D distance: 4
Path: A -> C -> D

A-E distance: 8
Path: A -> C -> E

A-F distance: 7
Path: A -> B -> F
```

## Autor
- Curso: Scientific Computing with Python
- Parte 8: Learn Algorithm Design by Building a Shortest Path Algorithm