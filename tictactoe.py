"""
Tic Tac Toe Player
"""

import math
import copy

X = "X" # Maximizer
O = "O" # Minimizer
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    
    xMoves = 0
    oMoves = 0
    for row in board:
        for cell in row:
            if cell == X:
                xMoves += 1
            elif cell == O:
                oMoves += 1

    if xMoves > oMoves:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possibleActions.add((row, col))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    
    resultBoard = copy.deepcopy(board)
    resultBoard[action[0]][action[1]] = player(board)
    return resultBoard
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in range(3): # previous was also working, but this is easier to read
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (winner(board) is None and not any(EMPTY in sublist for sublist in board)):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

# helper function for minimax
def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

# helper function for minimax
def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if board == initial_state():
        return (0, 0)
    
    if player(board) == X:
        best_move = None
        best_value = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:
        best_move = None
        best_value = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_move
