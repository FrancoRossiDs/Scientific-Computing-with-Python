# Número de discos con los que vamos a trabajar
NUMBER_OF_DISKS = 3

# Representación de las torres (listas)
# A comienza con los discos (del más grande al más chico)
# B y C comienzan vacías
A = list(range(NUMBER_OF_DISKS, 0, -1))  # [3, 2, 1]
B = []
C = []

# Estado inicial
print(A, B, C, '\n')

def move(n, source, auxiliary, target):
    """
    Mueve n discos desde 'source' hasta 'target',
    usando 'auxiliary' como torre de apoyo.
    """

    if n <= 0:
        return
    
    # 1. Mover los primeros n-1 discos de 'source' a 'auxiliary'
    #    (esto libera el disco más grande, que está al fondo)
    move(n - 1, source, target, auxiliary)
    
    # 2. Mover el disco más grande (el disco n) de 'source' a 'target'
    target.append(source.pop())
    
    # Mostrar el estado actual de las torres después de cada movimiento
    print(A, B, C, '\n')
    
    # 3. Mover los n-1 discos que quedaron en 'auxiliary' hacia 'target'
    move(n - 1, auxiliary, source, target)

# Llamada inicial: mover todos los discos desde A hasta C, usando B de apoyo
move(NUMBER_OF_DISKS, A, B, C)