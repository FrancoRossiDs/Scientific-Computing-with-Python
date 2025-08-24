# Lambda Function - Expense Tracker

Este mini proyecto es un rastreador de gastos simple en Python que utiliza funciones lambda y programación funcional para gestionar y analizar gastos.

## Archivos
- `main.py`: Contiene la lógica para agregar, listar, filtrar y sumar gastos usando funciones lambda.

## ¿Cómo funciona?
El programa permite al usuario:
- Agregar un gasto con monto y categoría.
- Listar todos los gastos ingresados.
- Calcular el total de gastos.
- Filtrar gastos por categoría.

Utiliza funciones lambda para sumar y filtrar los gastos de manera eficiente.

### Ejemplo de uso
```python
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Ejemplo de interacción
```
Expense Tracker
1. Add an expense
2. List all expenses
...
```

## Autor
- Curso: Scientific Computing with Python
- Parte 3: Learn Lambda Functions by Building an Expense Tracker
