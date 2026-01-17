# Binary Search Tree - Mini Project

This mini project implements a Binary Search Tree (BST) in Python with insertion, search, deletion, and traversal operations.

## Files
- `main.py`: Contains the TreeNode and BinarySearchTree classes with complete BST functionality and usage examples.

## How does it work?
The program defines two classes:
- **TreeNode**: Represents a node in the tree with a key value and references to left and right children.
- **BinarySearchTree**: Implements the BST data structure with the following operations:
  - **Insert**: Adds a new node to the tree maintaining BST properties
  - **Search**: Finds a node with a specific key value
  - **Delete**: Removes a node from the tree while preserving BST structure
  - **Inorder Traversal**: Returns all elements in sorted order

### Example usage
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

## Run
To run the program, use:

```bash
python main.py
```

## Expected output
```
Search for 80: 80
Inorder traversal: [20, 30, 40, 50, 60, 70, 80]
Search for 40: None
Inorder traversal after deleting 40: [20, 30, 50, 60, 70, 80]
```

## Author
- Course: Scientific Computing with Python
- Part 11: Learn Tree Traversal by Building a Binary Search Tree

---
You can modify the tree to test different operations and node arrangements if you wish.
