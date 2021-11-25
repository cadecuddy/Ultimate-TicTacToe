import math
import random


class Board:

    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __str__(self):
        output = ""
        for row in self.board:
            output += "| "
            for col in row:
                output += str(col) + " | "
            output += "\n"
        return output

    def isTerminal(self):
        # Check if board filled up
        return not any(0 in row for row in self.board)

    def possibleMoves(self):
        moves = 0
        for row in self.board:
            moves += row.count(0)
        return moves

    def winner(self, id, square):
        # check if a move that has been made has won the game
        row = math.floor((square - 1) / 3)
        col = (square - 1) % 3

        # Horizontal Win
        if all([x == id for x in self.board[row]]):
            return True

        # Vertical Win
        column = [row[col] for row in self.board]
        if all([x == id for x in column]):
            return True

        # Diagonal Win
        if square % 2 != 0:
            left_diagonal = [self.board[x - 1][x - 1] for x in range(1, 4)]
            right_diagonal = [self.board[x - 1][3 - x] for x in range(1, 4)]
            if all([x == id for x in right_diagonal]) or all([x == id for x in left_diagonal]):
                return True

        return False

    def make_move(self, square, id):
        # Makes a move on the board given a square number 1-9,
        # provided the given square is available, marks square with player id (1 or -1)
        if square not in range(1, 10):
            raise ValueError("Invalid square")

        row = math.floor((square - 1) / 3)
        col = (square - 1) % 3

        if self.board[row][col] == 0:
            self.board[row][col] = id
            return True
        return False


class Player:
    # board is board class object
    def make_move(self, board, square):
        # Makes a move on the board given a square number 1-9,
        # provided the given square is available
        if square not in range(1, 10):
            raise ValueError("Invalid square")

        board.make_move(square, 1)


class AIPlayer:

    def make_ai_move(self, board):
        # If board is empty, random first move
        if board.possibleMoves() == 0:
            board.make_move(random.randint(1, 9), -1)
        else:
            self.minimax()
        return

    def minimax(self, board, maximizing):
        id = 1
        if maximizing:
            id = -1
        if self.isTerminal():
            if self.winner() == 0:
                return 0
            else:
                return self.winner()

        scores = []
        # go through all possible moves

        return


b = Board()
# print(b.possibleMoves())
# # print(b)
# # for x in range(1, 10):
# #     b.make_move(1, x)
# #     print(b)
while not b.isTerminal():
    try:
        s = int(input("Pick a square 1 - 9: "))
        b.make_move(s, 1)
        print(b)
        if b.winner(1, s):
            print(
                f"\nPlayer has won the game with the winning move on the {s} square!")
            break
    except ValueError:
        print("Enter a valid square number.")
        continue
