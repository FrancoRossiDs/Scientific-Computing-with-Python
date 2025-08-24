# Cipher Mini Proyecto

Este proyecto es una implementación simple del cifrado de Vigenère en Python. Permite cifrar y descifrar mensajes utilizando una clave personalizada.

## Archivos
- `main.py`: Contiene toda la lógica para cifrar y descifrar mensajes usando el cifrado de Vigenère.

## ¿Cómo funciona?
El programa toma un texto cifrado y una clave personalizada, y utiliza el algoritmo de Vigenère para descifrar el mensaje. También puede cifrar cualquier texto que ingreses.

### Ejemplo de uso
```python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

decryption = decrypt(text, custom_key)
print(decryption)  # Salida: freecodecamp is awesome
```

## Ejecución
Para ejecutar el programa, simplemente corre:

```bash
python Cipher/main.py
```

## Salida esperada
```
Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding

Decrypted text: freecodecamp is awesome
```

## Autor
- Curso: Scientific Computing with Python
- Parte 1: Learn String Manipulation by Building a Cipher

---
¡Puedes modificar la clave y el texto para probar diferentes resultados!
