import re         # Para usar expresiones regulares (validar condiciones de la contraseña)
import secrets    # Para generar valores aleatorios seguros (mejor que random para seguridad)
import string     # Contiene letras, dígitos y símbolos predefinidos


# ---------------- FUNCION PRINCIPAL ----------------
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Genera una contraseña segura cumpliendo con ciertos requisitos:
    - length: longitud de la contraseña
    - nums: cantidad mínima de números
    - special_chars: cantidad mínima de caracteres especiales
    - uppercase: cantidad mínima de mayúsculas
    - lowercase: cantidad mínima de minúsculas
    """

    # Conjuntos de caracteres que podemos usar
    letters = string.ascii_letters   # Todas las letras (A-Z y a-z)
    digits = string.digits           # Todos los números (0-9)
    symbols = string.punctuation     # Todos los caracteres especiales (!, @, #, ...)

    # Unimos todos los caracteres posibles en una sola "bolsa"
    all_characters = letters + digits + symbols

    # Bucle infinito hasta generar una contraseña válida
    while True:
        password = ''
        
        # Generamos una contraseña al azar de la longitud pedida
        for _ in range(length):
            # secrets.choice → elige un carácter aleatorio de manera segura
            password += secrets.choice(all_characters)
        
        # Lista de restricciones a verificar en la contraseña
        constraints = [
            # Se pide al menos "nums" dígitos → \d significa números en regex
            (nums, r'\d'),
            # Al menos "special_chars" símbolos → usamos los símbolos definidos
            (special_chars, fr'[{symbols}]'),
            # Al menos "uppercase" letras mayúsculas
            (uppercase, r'[A-Z]'),
            # Al menos "lowercase" letras minúsculas
            (lowercase, r'[a-z]')
        ]

        # Validamos TODAS las restricciones
        # → re.findall busca todos los caracteres que coinciden con el patrón
        # → len(...) cuenta cuántos se encontraron
        # → Se verifica que la cantidad encontrada sea >= a lo requerido
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break   # Si cumple todas las condiciones, salimos del while
    
    return password



# ---------------- BLOQUE PRINCIPAL ----------------
if __name__ == '__main__':
    # Llamamos a la función con los valores por defecto (16 caracteres)
    new_password = generate_password()
    print('Generated password:', new_password)