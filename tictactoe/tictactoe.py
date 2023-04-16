"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
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
    count_O, count_X = 0, 0
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == O:
                count_O += 1
            elif board[row][column] == X:
                count_X += 1
            else:
                raise Exception('Something wrong!')
    return O if count_X != count_O else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == EMPTY:
                possible_actions.add((row, column))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i, j) = action
    if i < 0 or i > (len(board) - 1) or j < 0 or j > (len(board) - 1):
        raise IndexError
    res_board = copy.deepcopy(board)
    res_board[i][j] = player(board)
    return res_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
