from tictactoe import *
import pytest


def test_initial_state():
    assert initial_state() == [[EMPTY, EMPTY, EMPTY],
                               [EMPTY, EMPTY, EMPTY],
                               [EMPTY, EMPTY, EMPTY]]

def test_player():
    board1 = [[X, O, EMPTY],
              [EMPTY, X, X],
              [EMPTY, EMPTY, O]]
    board2 = [[X, O, X],
              [EMPTY, O, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
    assert player(board1) == O
    assert player(board2) == X

def test_actions():
    board = [[X, O, X],
             [O, X, O],
             [X, O, EMPTY]]
    assert actions(board) == {(2, 2)}

def test_result():
    board = [[X, O, EMPTY],
              [EMPTY, X, X],
              [EMPTY, EMPTY, O]]
    action = (1, 0)
    new_board = result(board, action)
    assert new_board == [[X, O, EMPTY],
              [O, X, X],
              [EMPTY, EMPTY, O]]
    assert player(new_board) == X

def test_winner():
    board1 = [[X, O, X],
              [X, X, O],
              [O, X, O]]
    board2 = [[X, O, X],
              [O, X, EMPTY],
              [X, O, EMPTY]]
    board3 = [[X, O, X],
              [O, O, EMPTY],
              [X, O, X]]
    
    assert winner(board1) == None
    assert winner(board2) == X
    assert winner(board3) == O

def test_terminal():
    board1 = [[X, O, X],
              [X, X, O],
              [O, X, O]]
    board2 = [[X, O, X],
              [O, X, EMPTY],
              [X, O, EMPTY]]
    board3 = [[X, EMPTY, X],
              [EMPTY, O, EMPTY],
              [EMPTY, EMPTY, O]]
    
    assert terminal(board1) == True
    assert terminal(board2) == True
    assert terminal(board3) == False

def test_utility():
    board1 = [[X, O, X],
              [X, X, O],
              [O, X, O]]
    board2 = [[X, O, X],
              [O, X, EMPTY],
              [X, O, EMPTY]]
    board3 = [[X, O, X],
              [O, O, EMPTY],
              [X, O, X]]
    assert utility(board1) == 0
    assert utility(board2) == 1
    assert utility(board3) == -1

def test_minimax():
    board1 = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
    board2 = [[X, O, X],
              [O, X, EMPTY],
              [X, O, EMPTY]]
    assert minimax(board1) == (0, 0) 
    assert minimax(board2) == None

def test_max_value():
    board = [[X, O, X],
             [O, X, O],
             [X, O, EMPTY]]
    assert max_value(board) == 1

def test_min_value():
    board = [[X, O, X],
             [X, O, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    assert min_value(board) == -1

if __name__ == "__main__":
    pytest.main()
