# Acomodador Aritmético

Este proyecto proporciona una función en Python llamada `arithmetic_arranger` que formatea una lista de problemas aritméticos simples (suma y resta) de la misma manera en que los estudiantes de primaria los acomodan verticalmente para facilitar su resolución.

## Características
- Acomoda los problemas aritméticos de forma vertical y uno al lado del otro.
- Soporta únicamente sumas y restas.
- Opcionalmente muestra las respuestas de los problemas.
- Devuelve mensajes de error claros para entradas inválidas.

## Uso

Importa o utiliza la función `arithmetic_arranger` en tu código Python:

```python
from main import arithmetic_arranger

# Ejemplo de uso:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
```

### Ejemplo de salida
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
Con respuestas:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Reglas y validaciones
- Máximo de cinco problemas por llamada. Si hay más, devuelve: `Error: Too many problems.`
- Solo se permiten sumas y restas. Otros operadores devuelven: `Error: Operator must be '+' or '-'.`
- Los operandos deben contener solo dígitos. De lo contrario: `Error: Numbers must only contain digits.`
- Los operandos deben tener como máximo cuatro dígitos. Si no: `Error: Numbers cannot be more than four digits.`
- Los problemas se formatean con números alineados a la derecha, un solo espacio entre el operador y el operando, y cuatro espacios entre cada problema.

## Estructura de archivos
- `main.py`: Contiene la implementación de la función.
- `consigna.md`: Instrucciones y requisitos del proyecto.

## Autor
- Curso: Scientific Computing with Python
- Primer proyecto: Build an Arithmetic Formatter Project

---
Podes probar otras cuentas para ver los cambios
