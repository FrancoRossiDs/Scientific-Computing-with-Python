# Grafo representado como diccionario
# Cada nodo tiene una lista de tuplas (vecino, peso)
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


def shortest_path(graph, start, target=''):
    """
    Calcula la distancia más corta desde un nodo de inicio `start`
    hacia todos los demás nodos (o hacia uno específico `target`)
    usando una variación del algoritmo de Dijkstra.
    """

    # Lista de nodos que aún no fueron visitados
    unvisited = list(graph)

    # Diccionario con las distancias mínimas desde el inicio a cada nodo
    # → al inicio, start = 0 y el resto = infinito
    distances = {node: 0 if node == start else float('inf') for node in graph}

    # Diccionario con los caminos más cortos encontrados
    # Cada clave guarda la secuencia de nodos desde start hasta ese nodo
    paths = {node: [] for node in graph}
    paths[start].append(start)  # El camino hacia sí mismo es solo "start"
    
    # Mientras queden nodos por visitar
    while unvisited:
        # Elegimos el nodo con la distancia mínima hasta ahora
        current = min(unvisited, key=distances.get)

        # Revisamos todos los vecinos del nodo actual
        for node, distance in graph[current]:
            # Nueva distancia = distancia actual + peso de la arista
            if distance + distances[current] < distances[node]:
                # Si encontramos un camino más corto → lo actualizamos
                distances[node] = distance + distances[current]

                # Actualizamos el camino hasta ese nodo
                if paths[node] and paths[node][-1] == node:
                    # Si ya había un camino, lo reemplazamos
                    paths[node] = paths[current][:]
                else:
                    # Si no, extendemos el camino actual
                    paths[node].extend(paths[current])

                # Finalmente añadimos el nodo al camino
                paths[node].append(node)

        # Marcamos el nodo como visitado
        unvisited.remove(current)
    
    # Si se pidió un destino específico → solo mostramos ese
    # Si no → mostramos todos los caminos
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue  # No mostramos la distancia de start a start
        print(f'\n{start}-{node} distance: {distances[node]}')
        print(f'Path: {" -> ".join(paths[node])}')
    
    return distances, paths


# Llamada a la función: desde A a todos los nodos
shortest_path(my_graph, 'A')