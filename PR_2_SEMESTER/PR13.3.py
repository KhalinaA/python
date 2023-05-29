import random

class Board:
    def __init__(self):
        self.cells = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.cells:
            print('|', end=' ')
            print(*row, sep=' | ', end=' |\n')

    def make_move(self, player, row, col):
        if self.cells[row][col] == ' ':
            self.cells[row][col] = player.symbol
            return True
        else:
            return False

    def is_full(self):
        for row in self.cells:
            if ' ' in row:
                return False
        return True

    def is_winner(self, player):
        symbol = player.symbol

        for row in self.cells:
            if all(cell == symbol for cell in row):
                return True

        for col in range(3):
            if self.cells[0][col] == symbol and self.cells[1][col] == symbol and self.cells[2][col] == symbol:
                return True

        if self.cells[0][0] == symbol and self.cells[1][1] == symbol and self.cells[2][2] == symbol:
            return True

        if self.cells[0][2] == symbol and self.cells[1][1] == symbol and self.cells[2][0] == symbol:
            return True

        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        row = int(input("Введите номер строки (0-2): "))
        col = int(input("Введите номер столбца (0-2): "))
        return row, col


class ComputerPlayer(Player):
    def get_move(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return row, col


def play_game():
    board = Board()
    player1_name = input("Введите имя первого игрока: ")
    player1_symbol = input("Введите символ первого игрока (X или O): ")
    player1 = Player(player1_name, player1_symbol)

    if player1_symbol.upper() == 'X':
        player2_symbol = 'O'
    else:
        player2_symbol = 'X'

    play_with_computer = input("Хотите играть с компьютером? (Да/Нет): ")

    if play_with_computer.lower() == 'да':
        player2 = ComputerPlayer("Компьютер", player2_symbol)
    else:
        player2_name = input("Введите имя второго игрока: ")
        player2 = Player(player2_name, player2_symbol)

    current_player = player1

    while True:
        board.display()
        print(f"Ход игрока {current_player.name}")

        row, col = current_player.get_move()

        while not board.make_move(current_player, row, col):
            print("Некорректный ход. Попробуйте снова.")
            row, col = current_player.get_move()

        if board.is_winner(current_player):
            board.display()
            print(f"Победил игрок {current_player.name}!")
            break
        elif board.is_full():
            board.display()
            print("Ничья!")
            break

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1


play_game()
