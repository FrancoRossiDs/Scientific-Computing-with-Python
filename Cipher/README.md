# Cipher Mini Project

This project is a simple implementation of the Vigenère cipher in Python. It allows you to encrypt and decrypt messages using a custom key.

## Files
- `main.py`: Contains all the logic to encrypt and decrypt messages using the Vigenère cipher.

## How does it work?
The program takes an encrypted text and a custom key, and uses the Vigenère algorithm to decrypt the message. It can also encrypt any text you enter.

### Example usage
```python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

decryption = decrypt(text, custom_key)
print(decryption)  # Output: freecodecamp is awesome
```

## Run
To run the program, simply execute:

```bash
python Cipher/main.py
```

## Expected output
```
Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding

Decrypted text: freecodecamp is awesome
```

## Author
- Course: Scientific Computing with Python
- Part 1: Learn String Manipulation by Building a Cipher

---
You can change the key and text to try different results!
