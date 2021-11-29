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

    def undo(self):
        # Undo the most recent move
        row = math.floor((self.recent_move - 1) / 3)
        col = (self.recent_move - 1) % 3
        self.board[row][col] = 0

    def possibleMoves(self):
        moves = []
        r = 0
        for row in self.board:
            c = 0
            for col in row:
                c += 1
                if col == 0:
                    moves.append((3 * r) + c)
            r += 1
        return moves

    def get_winner(self):
        row = math.floor((self.recent_move - 1) / 3)
        col = (self.recent_move - 1) % 3
        return self.board[row][col]

    def winner(self):
        # check if the most recent move that has been made has won the game
        # and return the winner's id
        row = math.floor((self.recent_move - 1) / 3)
        col = (self.recent_move - 1) % 3

        # Horizontal Win
        if all([x == self.board[row][col] for x in self.board[row]]):
            return True

        # Vertical Win
        column = [row[col] for row in self.board]
        if all([x == self.board[row][col] for x in column]):
            return True

        # Diagonal Win
        if self.recent_move % 2 != 0:
            left_diagonal = [self.board[x - 1][x - 1] for x in range(1, 4)]
            right_diagonal = [self.board[x - 1][3 - x] for x in range(1, 4)]
            if all([x == self.board[row][col] for x in right_diagonal]) or all([x == self.board[row][col] for x in left_diagonal]):
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
            self.recent_move = square
            return True
        raise ValueError("Already a thing")


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
        if len(board.possibleMoves()) == 9:
            board.make_move(random.randint(1, 9), -1)
        else:
            self.optimal_move(board)

    def optimal_move(self, board):
        # TODO: Use minimax to find optimal move
        return -1

    def minimax(self, board, maximizing):
        id = -1
        if maximizing:
            id = 1
        # If game is a draw
        if board.isTerminal() and not board.winner():
            return 0
        elif board.winner():
            return 1 if board.get_winner() == id else -1

        scores = []
        # go through all possible moves
        for move in board.possibleMoves():
            board.make_move(move, id)
            scores.append(self.minimax(board, not maximizing))
            board.undo()

        return max(scores) if maximizing else min(scores)


b = Board()
# Game loop (to play against random AI)
turn = True
while True:
    if turn:
        try:
            s = int(input("Pick a square 1 - 9: "))
            b.make_move(s, 1)
            print(b)
            turn = not turn
        except ValueError:
            print("Enter a valid square number.")
            continue
    else:
        ai = random.choice(b.possibleMoves())
        b.make_move(ai, -1)
        print(f"AI picked square {ai}.")
        print(b)
        turn = True

    if b.isTerminal() or b.winner():
        print(
            f"\n{b.get_winner()} has won the game!")
        break
