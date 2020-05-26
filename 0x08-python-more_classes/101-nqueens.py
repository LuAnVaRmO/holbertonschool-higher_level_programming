#!/usr/bin/python3
"""
nQueen
"""


class Nqueen:
    """ Class nQueen """
    def __init__(self, number, board):
        self.number = number
        self.board = board

    @property
    def number(self):
        """ Getter function """
        return self.__number

    @number.setter
    def number(self, value):
        """ Setter function """
        self.__number = value

    @property
    def board(self):
        """ Getter function"""
        return self.__board

    @board.setter
    def board(self, value):
        """ Setter function """
        self.__board = value

    def print_board(self):
        """ printing board """
        for i in range(self.number):
            for j in range(self.number):
                print(self.board[i][j], end="")
            print()

    def verification(self):
        """ verifying positions """
        n1 = 0
        n2 = 0
        temp = 0
        count = 0

        self.__board[n1][n2] = 1
        for row in range(self.__number):
            for col in range(self.__number):
                if self.__board[row][col] == 1:
                    if row == col:
                        self.__board[row][col] = 1
                else:
                    pass
        self.print_board()





if __name__ == "__main__":
    from sys import argv

    if len(argv) is not 2:
        print("Usage: nqueens N")
        exit(1)
    if type(int(argv[1])) is not int:
        print("N must be a number")
        exit(1)
    num = int(argv[1])
    if num < 4:
        print("N must be at least 4")
        exit(1)
    matrix = [[0] * num] * num
    q = Nqueen(num, matrix)
    q.print_board()
    print("----")
    q.verification()
