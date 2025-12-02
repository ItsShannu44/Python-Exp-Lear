# Chess Game is played with a board and a pieces that are pawns, rooks, bishop, king, queen...

# Component class

class Piece:
    def __init__(self, color):
        self.color = color

# Pawn is a type of piece
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'Pawn'

# Board has eight Pawns of each color. (has is used so composition)
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] 
                     for _ in range(8)]
        
    def initialize_board(self):
        '''Creating pawns to be placed on second and last but 
           second row'''
        self.grid[1] = [Pawn('White') for _ in range(8)]
        self.grid[6] = [Pawn('Black') for _ in range(8)]

    def print_board(self):
        for row in self.grid:
            print([piece.type if piece else '----' for piece in row])

# Composite Class - Game
class Game:
    def __init__(self):
        self.board = Board()
        self.board.initialize_board()

    def play(self):
        print('Initial Board Arrangement')
        self.board.print_board()

# Begin the game
Game().play()