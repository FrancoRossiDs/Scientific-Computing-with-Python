# Regular Expressions - Password Generator

This project is a secure password generator in Python that uses regular expressions to ensure the generated password meets certain requirements.

## Features
- Generates a random password of customizable length (default: 16 characters).
- Ensures the password contains at least:
  - A specified number of digits
  - A specified number of special characters
  - A specified number of uppercase letters
  - A specified number of lowercase letters
- Uses the `secrets` module for cryptographically secure random generation.
- Uses regular expressions to validate password constraints.

## Files
- `main.py`: Contains the password generation logic and an example of usage.

## How it works
The function `generate_password` generates a password that meets the specified constraints. It keeps generating passwords until all requirements are satisfied, using regular expressions to check for digits, special characters, uppercase, and lowercase letters.

### Example usage
```python
new_password = generate_password(length=20, nums=2, special_chars=2, uppercase=2, lowercase=2)
print('Generated password:', new_password)
```

## Running the program
To run the program, use:

```bash
python main.py
```

## Example output
```
Generated password: 8@Aq!b2Zx#1Lp$wR
```

## Author
- Course: Scientific Computing with Python
- Part 7: Learn Regular Expressions by Building a Password Generator