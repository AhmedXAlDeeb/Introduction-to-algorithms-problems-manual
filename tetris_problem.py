"""
This short program solves the problem of tetris using dynamic programming
"""
import numpy as np
from collections import defaultdict
class Tetris():
    def __init__(self, width=10, height=10):
        self.board = np.zeros((height, width), dtype=int)
        self.pieces = [
            np.array([[1, 1, 1, 1]]),
            np.array([[1, 1], [1, 1]]),
            np.array([[0, 1, 0], [1, 1, 1]]),
            np.array([[1, 0], [1, 0], [1, 1]])
        ]
        self.width = width
        self.height = height
        self.dp = defaultdict(lambda: float('inf'))
        self.dp[(0, tuple([0]*self.width))] = 0 # empty board
        self.pieces_sequence = None
        
    def add_piece(self, piece):
        self.pieces.append(piece)
        
    def construct_new_board(self, width, height):
        self.board = np.zeros((height,width), dtype= int)
        self._set_width()
        self._set_height()
        
    def _set_width(self):
        self.width = len(self.board[0])
    
    def _set_height(self):
        self.height = len(self.board)
    
    def place_piece(self, piece):
        for col in range(self.width):
            if self._can_place_piece(piece):
                loss = self._evluate_board_status(piece, col)
                return loss
    
    def _evaluate_board_status(self, piece, col):
        """
        The cost funtion which penalties the gaps and height
        """
        
    def _can_place_piece(self, piece, x,y):
        h, w = piece.shape
        
        #check if the piece will get out of the boundaries
        if y + h > self.height or x + w > self.width:
            return False
        
        for i in range(h):
            for j in range(w):
                #check if any cell is occupied before
                if piece[i, j] == 1 and self.board[x+i, y+j] == 1:
                    return False
        
        return True

    def solve_tetris(self):
        #the state variables are the current piece and the board status
        #board status can be a tuple of columns heights 
        # the state space can be sparse
        # so we will implement it in a dict
        for i, piece in enumerate(self.pieces_sequence):
            current_dp =defaultdict(lambda: float('inf'))
            for board, cost in self.dp.items():
                for x in range(self.width - piece.shape[1] +1):
                    new_board, placemen_cost = self.place_piece(board, piece, x)
                    new_cost = cost + placemen_cost
                    current_dp[new_board] = min(current_dp[new_board], new_cost)
                    
            self.dp = current_dp
                    
        