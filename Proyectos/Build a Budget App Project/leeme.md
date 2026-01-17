# Proyecto Construir una Aplicación de Presupuesto

Este proyecto implementa una aplicación de presupuesto en Python que gestiona diferentes categorías de presupuesto con un sistema de libro mayor, permitiendo depósitos, retiros, transferencias y una representación visual del porcentaje de gastos.

## Archivos
- `main.py`: Contiene la implementación de la clase Category y la función create_spend_chart.

## ¿Cómo funciona?
La clase `Category` representa una categoría de presupuesto y mantiene un libro mayor de transacciones. Admite:
- **deposit**: Añadir dinero a una categoría con una descripción opcional
- **withdraw**: Retirar dinero de una categoría si hay fondos disponibles
- **get_balance**: Recuperar el saldo actual
- **transfer**: Transferir dinero entre categorías
- **check_funds**: Verificar si hay fondos suficientes disponibles
- **__str__**: Mostrar el libro mayor de la categoría en una tabla formateada

La función `create_spend_chart` genera un gráfico de barras visual que muestra el porcentaje de gasto total para cada categoría.

### Ejemplo de uso
```python
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```

## Ejecución
Para ejecutar el programa, usa:

```bash
python main.py
```

## Salida esperada
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

## Autor
- Franco Rossi
- Tercer Proyecto: Construir una Aplicación de Presupuesto
---
Puedes modificar los valores de entrada y categorías para probar diferentes escenarios.
