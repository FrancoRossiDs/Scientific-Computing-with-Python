# Expresiones Regulares - Generador de Contraseñas

Este proyecto es un generador seguro de contraseñas en Python que utiliza expresiones regulares para asegurar que la contraseña generada cumpla ciertos requisitos.

## Características
- Genera una contraseña aleatoria de longitud personalizable (por defecto: 16 caracteres).
- Asegura que la contraseña contenga al menos:
  - Una cantidad específica de dígitos
  - Una cantidad específica de caracteres especiales
  - Una cantidad específica de letras mayúsculas
  - Una cantidad específica de letras minúsculas
- Utiliza el módulo `secrets` para una generación aleatoria criptográficamente segura.
- Utiliza expresiones regulares para validar los requisitos de la contraseña.

## Archivos
- `main.py`: Contiene la lógica de generación de contraseñas y un ejemplo de uso.

## ¿Cómo funciona?
La función `generate_password` genera una contraseña que cumple con los requisitos especificados. Sigue generando contraseñas hasta que todas las condiciones se cumplen, usando expresiones regulares para verificar dígitos, caracteres especiales, mayúsculas y minúsculas.

### Ejemplo de uso
```python
new_password = generate_password(length=20, nums=2, special_chars=2, uppercase=2, lowercase=2)
print('Generated password:', new_password)
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Ejemplo de salida
```
Generated password: 8@Aq!b2Zx#1Lp$wR
```

## Autor
- Curso: Scientific Computing with Python
- Parte 7: Learn Regular Expressions by Building a Password Generator