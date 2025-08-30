def convert_to_snake_case(pascal_or_camel_cased_string):
    # Construimos una lista de caracteres transformados
    # Si el caracter es mayúscula, le anteponemos '_' y lo convertimos a minúscula
    # Si no es mayúscula, lo dejamos igual
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    # Unimos todos los caracteres en un string y quitamos un posible '_' inicial
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Ejemplo: "IAmAPascalCasedString"
    # → "_i_am_a_pascal_cased_string" → "i_am_a_pascal_cased_string"
    print(convert_to_snake_case('IAmAPascalCasedString'))

# Llamamos a main() para ejecutar el programa
main()
