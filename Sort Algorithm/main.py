def merge_sort(array):
    """
    Implementación del algoritmo Merge Sort (Ordenamiento por mezcla).
    Divide el arreglo en mitades recursivamente, y luego las combina
    en orden hasta obtener el arreglo completamente ordenado.
    """

    # Caso base: si el arreglo tiene 0 o 1 elementos, ya está ordenado
    if len(array) <= 1:
        return
    
    # 1. Dividir el arreglo en dos mitades
    middle_point = len(array) // 2
    left_part = array[:middle_point]   # Desde el inicio hasta el medio (sin incluirlo)
    right_part = array[middle_point:]  # Desde el medio hasta el final

    # 2. Ordenar recursivamente cada mitad
    merge_sort(left_part)
    merge_sort(right_part)

    # 3. Combinar las dos mitades ordenadas en un solo arreglo
    left_array_index = 0    # Índice para recorrer la mitad izquierda
    right_array_index = 0   # Índice para recorrer la mitad derecha
    sorted_index = 0        # Índice para ir colocando elementos en el arreglo original

    # Comparar elementos de ambas mitades y copiar el menor al arreglo original
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copiar los elementos restantes de la mitad izquierda (si quedaron)
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Copiar los elementos restantes de la mitad derecha (si quedaron)
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    # Ejemplo de uso
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)

    # Llamamos al algoritmo
    merge_sort(numbers)

    # Imprimimos el arreglo ya ordenado
    print('Sorted array: ' + str(numbers))