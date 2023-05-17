import random

class Cell:
    def __init__(self, number):
        self.value = ' '
        self.number = number

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]
        self.current_player = None

    def print_board(self):
        print('-------------')
        print('| ' + self.cells[0].value + ' | ' + self.cells[1].value + ' | ' + self.cells[2].value + ' |')
        print('-------------')
        print('| ' + self.cells[3].value + ' | ' + self.cells[4].value + ' | ' + self.cells[5].value + ' |')
        print('-------------')
        print('| ' + self.cells[6].value + ' | ' + self.cells[7].value + ' | ' + self.cells[8].value + ' |')
        print('-------------')

