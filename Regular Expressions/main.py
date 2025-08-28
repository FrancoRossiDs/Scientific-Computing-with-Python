import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        # Define the constraints
        constraints = [
            # Number of digits
            (nums, r'\d'),
            # Number of special characters
            (special_chars, fr'[{symbols}]'),
            # Number of uppercase characters
            (uppercase, r'[A-Z]'),
            # Number of lowercase characters
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            # Check for at least one character from each required set
            for constraint, pattern in constraints
        ):
            break
    
    return password
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)