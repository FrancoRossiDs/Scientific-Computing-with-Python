def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Calcula la raíz cuadrada de un número usando el método de bisección.
    Parámetros:
        square_target: número al cual se le quiere calcular la raíz cuadrada.
        tolerance: margen de error aceptable entre la aproximación y el valor real.
        max_iterations: número máximo de iteraciones para evitar bucles infinitos.
    """

    # Caso inválido: no existe raíz cuadrada real de números negativos
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    # Casos triviales: raíz de 0 y 1 se conocen sin cálculos
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Inicializamos el intervalo [low, high]
        # La raíz cuadrada de un número N siempre estará entre 0 y max(1, N)
        low = 0
        high = max(1, square_target)
        root = None
        
        # Iteramos hasta encontrar una aproximación suficientemente buena
        for _ in range(max_iterations):
            # Tomamos el punto medio
            mid = (low + high) / 2
            square_mid = mid**2  # Elevamos al cuadrado para comparar con N

            # Verificamos si la aproximación es suficientemente precisa
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            # Si el cuadrado es menor al objetivo, desplazamos low hacia mid
            elif square_mid < square_target:
                low = mid
            # Si es mayor, desplazamos high hacia mid
            else:
                high = mid

        # Si no se logró la precisión en max_iterations iteraciones
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root


# Ejemplo de uso
N = 16
square_root_bisection(N)