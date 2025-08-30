# Merge Sort Algorithm - Mini Project

This project implements the Merge Sort algorithm in Python to sort a list of numbers.

## Files
- `main.py`: Contains the implementation of the merge sort algorithm and an example of its usage.

## How does it work?
The `merge_sort` function recursively divides the list into halves, sorts each half, and then merges them back together in sorted order. This is a classic example of a divide-and-conquer algorithm.

### Example usage
```python
def merge_sort(array):
    # ...code...

numbers = [4, 10, 6, 14, 2, 1, 8, 5]
print('Unsorted array: ')
print(numbers)
merge_sort(numbers)
print('Sorted array: ' + str(numbers))
```

## Running the program
To run the program, use:

```bash
python main.py
```

## Expected output
```
Unsorted array: 
[4, 10, 6, 14, 2, 1, 8, 5]
Sorted array: [1, 2, 4, 5, 6, 8, 10, 14]
```

## Author
- Franco Rossi
- Part 10: Learn Data Structures by Building the Merge Sort Algorithm
---
You can modify the list of numbers to sort different arrays as needed.
