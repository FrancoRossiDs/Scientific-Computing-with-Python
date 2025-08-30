# ---------------- FUNCIONES PRINCIPALES ----------------

# Agregar un gasto a la lista de gastos
def add_expense(expenses, amount, category):
    # Cada gasto se guarda como un diccionario con "monto" y "categoría"
    expenses.append({'amount': amount, 'category': category})
    

# Mostrar todos los gastos
def print_expenses(expenses):
    # Recorremos la lista de gastos y los imprimimos
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    

# Calcular el total de gastos
def total_expenses(expenses):
    # sum() + map() → recorremos todos los gastos y sumamos los montos
    return sum(map(lambda expense: expense['amount'], expenses))
    

# Filtrar gastos por categoría
def filter_expenses_by_category(expenses, category):
    # filter() devuelve un iterador con los gastos que cumplen la condición
    return filter(lambda expense: expense['category'] == category, expenses)
    


# ---------------- FUNCIÓN PRINCIPAL DEL PROGRAMA ----------------
def main():
    expenses = []  # lista vacía de gastos al iniciar
    
    while True:  # menú infinito hasta que el usuario elija salir
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')  # pedimos opción al usuario

        # ---------- OPCIÓN 1: agregar gasto ----------
        if choice == '1':
            amount = float(input('Enter amount: '))  # monto numérico
            category = input('Enter category: ')     # categoría en texto
            add_expense(expenses, amount, category)

        # ---------- OPCIÓN 2: mostrar gastos ----------
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        # ---------- OPCIÓN 3: mostrar total ----------
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        # ---------- OPCIÓN 4: filtrar por categoría ----------
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        # ---------- OPCIÓN 5: salir ----------
        elif choice == '5':
            print('Exiting the program.')
            break

# Ejecutar el programa
main()