def arithmetic_arranger(problems, show_answers=False):
    # Listas que guardarán cada "fila" de las operaciones
    linea1=[]   # primera fila (los números de arriba)
    linea2=[]   # segunda fila (operador y número de abajo)
    linea3=[]   # tercera fila (línea de guiones)
    linea4=[]   # cuarta fila (resultados, opcional)
    final_result=''  # string final a devolver

    # Recorremos cada problema de la lista
    for problem in problems:
        # Dividimos cada problema en: número1, operador, número2
        num1, operator, num2 = problem.split()

        # Calculamos el ancho de la operación
        # (número más largo + 2 espacios → uno para el operador y otro de margen)
        width = max(len(num1), len(num2)) + 2

        # ---------------- VALIDACIONES ----------------
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        elif not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        elif len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif len(problems) > 5:
            return "Error: Too many problems."

        # ---------------- RESOLVER ----------------
        # Calculamos el resultado como string (si show_answers=True lo mostraremos)
        if operator == '+':
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))
        
        # ---------------- FORMATO ----------------
        # rjust(width) → alinea a la derecha con el ancho definido

        # Primer número (arriba), alineado a la derecha
        linea1.append(num1.rjust(width))

        # Operador + segundo número (abajo), también alineado
        linea2.append(operator + num2.rjust(width - 1))

        # Línea de guiones del mismo largo que width
        linea3.append('-' * width)

        # ---------------- CONSTRUCCIÓN DEL TEXTO ----------------
        # Vamos uniendo cada línea con 4 espacios entre columnas
        final_result = '    '.join(linea1) + '\n' + \
                       '    '.join(linea2) + '\n' + \
                       '    '.join(linea3)

        # Si hay que mostrar respuestas, agregamos la cuarta fila
        if show_answers:
            linea4.append(result.rjust(width))
            final_result += '\n' + '    '.join(linea4)

    # Retornamos todo el string final (el "formato bonito")
    return final_result


# --------- PRUEBA ---------
# IMPORTANTE: máximo 5 operaciones
print(arithmetic_arranger(
    ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"],
    True  # mostrar respuestas
))