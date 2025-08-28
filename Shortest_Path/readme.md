# Shortest Path - Dijkstra's Algorithm Example

This project demonstrates how to find the shortest path in a weighted undirected graph using a simple implementation of Dijkstra's algorithm in Python.

## Features
- Calculates the shortest distance from a starting node to all other nodes in the graph.
- Prints the shortest path and distance for each node.
- The graph is represented as an adjacency list with weights.
- Easily adaptable to different graphs and starting points.

## Files
- `main.py`: Contains the graph definition, the shortest path function, and an example of usage.

## How it works
The function `shortest_path(graph, start, target='')` computes the shortest paths from the `start` node to all other nodes (or to a specific `target` node if provided) using a Dijkstra-like approach. It prints the distance and the path for each node.

### Example usage
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

## Running the program
To run the program, use:

```bash
python main.py
```

## Example output
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

## Author
- Course: Scientific Computing with Python
- Part 8: Learn Algorithm Design by Building a Shortest Path Algorithm