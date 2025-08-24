# Luhn Algorithm Mini Project

This project implements the Luhn algorithm in Python to verify the validity of credit card numbers.

## Files
- `main.py`: Contains the logic to validate a card number using the Luhn algorithm.

## How does it work?
The program takes a card number (which may contain dashes or spaces), cleans it, and checks if it is valid according to the Luhn algorithm.

### Example usage
```python
def verify_card_number(card_number):
    # ...code...

card_number = '4111-1111-4555-1142'
card_translation = str.maketrans({'-': '', ' ': ''})
translated_card_number = card_number.translate(card_translation)

if verify_card_number(translated_card_number):
    print('VALID!')
else:
    print('INVALID!')
```

## Run
To run the program, use:

```bash
python main.py
```

## Expected output
```
VALID!
```

## Author
- Course: Scientific Computing with Python
- Part 2: Learn How to Work with Numbers and Strings by Implementing the Luhn Algorithm