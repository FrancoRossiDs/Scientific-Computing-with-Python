# Case Converter - Mini Project

This mini project implements a Python function to convert strings from PascalCase or camelCase to snake_case.

## Files
- `main.py`: Contains the function to convert strings and an example of usage.

## How does it work?
The function `convert_to_snake_case` takes a PascalCase or camelCase string and converts it to snake_case, adding an underscore before each uppercase letter (except the first) and converting all letters to lowercase.

### Example usage
```python
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')

print(convert_to_snake_case('IAmAPascalCasedString'))  # Output: i_am_a_pascal_cased_string
```

## Run
To run the program, use:

```bash
python main.py
```

## Expected output
```
i_am_a_pascal_cased_string
```

## Author
- Course: Scientific Computing with Python
- Part 4: Learn Python List Comprehension by Building a Case Converter Program

---
You can modify the function to support other conversion formats if you wish.
