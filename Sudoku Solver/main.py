# Clase que representa un tablero de Sudoku
class Board:
    def __init__(self, board):
        # El tablero se recibe como una lista de listas (9x9)
        self.board = board

    def __str__(self):
        # Convierte el tablero en un string para poder imprimirlo de manera legible
        board_str = ''
        for row in self.board:
            # Si la celda es 0, mostramos '*' para indicar vacío
            row_str = [str(i) if i else '*' for i in row]
            # Unimos los números de la fila separados por espacio
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        # Busca la primera celda vacía (representada con 0)
        for row, contents in enumerate(self.board):
            try:
                # contents.index(0) busca la primera posición con 0
                col = contents.index(0)
                return row, col  # Devuelve la posición (fila, columna)
            except ValueError:
                # Si no hay 0 en esa fila, pasa a la siguiente
                pass
        return None  # Si no hay celdas vacías, devuelve None

    def valid_in_row(self, row, num):
        # Verifica que el número no esté repetido en la fila
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Verifica que el número no esté repetido en la columna
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        # Verifica que el número no esté repetido en el cuadrado 3x3
        # Calcula la esquina superior izquierda del cuadrado
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        # Recorre el cuadrado de 3x3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        # Revisa si un número puede colocarse en una celda vacía
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        # Solo es válido si cumple las tres condiciones
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        # Algoritmo recursivo para resolver el Sudoku (backtracking)
        
        # Busca la siguiente celda vacía
        if (next_empty := self.find_empty_cell()) is None:
            return True  # Si no hay vacías, el Sudoku está resuelto

        # Prueba con los números del 1 al 9
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess  # Coloca el número

                # Llama recursivamente para intentar resolver el resto
                if self.solver():
                    return True

                # Si no funcionó, resetea la celda y prueba con otro número
                self.board[row][col] = 0

        # Si ningún número funciona, hay que retroceder (backtracking)
        return False

# Función externa para resolver un Sudoku y mostrar el proceso
def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

# Ejemplo de Sudoku inicial (0 = celda vacía)
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Resolvemos el Sudoku
solve_sudoku(puzzle)