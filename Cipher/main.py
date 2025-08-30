# Texto cifrado que queremos descifrar
text = 'mrttaqrhknsw ih puggrur'

# Llave personalizada para cifrar/descifrar
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    # direction = 1 → cifrar
    # direction = -1 → descifrar
    
    key_index = 0                          # Posición actual en la clave
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # Alfabeto permitido
    final_message = ''                      # Resultado acumulado

    for char in message.lower():            # Recorremos cada caracter del mensaje
        # Si el caracter NO es letra (ej: espacio), se agrega tal cual
        if not char.isalpha():
            final_message += char
        else:
            # Tomamos la letra de la clave correspondiente a la posición actual
            # (se usa módulo para reiniciar si se termina la clave)
            key_char = key[key_index % len(key)]
            key_index += 1

            # Calculamos el "desplazamiento" en el alfabeto según la letra de la clave
            offset = alphabet.index(key_char)

            # Buscamos el índice de la letra actual en el alfabeto
            index = alphabet.find(char)

            # Calculamos el nuevo índice sumando o restando el offset
            # (depende de si ciframos o desciframos)
            new_index = (index + offset * direction) % len(alphabet)

            # Añadimos la nueva letra al mensaje final
            final_message += alphabet[new_index]

    return final_message

# Funciones auxiliares para que sea más claro
def encrypt(message, key):
    return vigenere(message, key, direction=1)

def decrypt(message, key):
    return vigenere(message, key, direction=-1)

# Programa principal
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

# Desciframos el mensaje usando la clave
decryption = decrypt(text, custom_key)

print(f'\nDecrypted text: {decryption}\n')
