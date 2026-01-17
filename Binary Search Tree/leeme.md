# Binary Search Tree - Mini Proyecto

Este mini proyecto implementa un Árbol de Búsqueda Binaria (BST) en Python con operaciones de inserción, búsqueda, eliminación y recorrido.

## Archivos
- `main.py`: Contiene las clases TreeNode y BinarySearchTree con la funcionalidad completa de BST y ejemplos de uso.

## ¿Cómo funciona?
El programa define dos clases:
- **TreeNode**: Representa un nodo en el árbol con un valor clave y referencias a los hijos izquierdo y derecho.
- **BinarySearchTree**: Implementa la estructura de datos BST con las siguientes operaciones:
  - **Insert**: Agrega un nuevo nodo al árbol manteniendo las propiedades del BST
  - **Search**: Encuentra un nodo con un valor clave específico
  - **Delete**: Elimina un nodo del árbol preservando la estructura del BST
  - **Inorder Traversal**: Devuelve todos los elementos en orden

### Ejemplo de uso
```python
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))
print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)
print("Search for 40:", bst.search(40))
print('Inorder traversal after deleting 40:', bst.inorder_traversal())
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Salida esperada
```
Search for 80: 80
Inorder traversal: [20, 30, 40, 50, 60, 70, 80]
Search for 40: None
Inorder traversal after deleting 40: [20, 30, 50, 60, 70, 80]
```

## Autor
- Curso: Scientific Computing with Python
- Parte 11: Learn Tree Traversal by Building a Binary Search Tree

---
Puedes modificar el árbol para probar diferentes operaciones y arreglos de nodos si lo deseas.
