"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
winnerMoves = [
      [(0,0),(0,1),(0,2)],
      [(1,0),(1,1),(1,2)],
      [(2,0),(2,1),(2,2)],
      [(0,0),(1,1),(2,2)],
      [(0,2),(1,1),(2,0)],
      [(0,0),(1,0),(2,0)],
      [(0,1),(1,1),(2,1)],
      [(0,2),(1,2),(2,2)]
    ]


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
    x = 0
    o = 0
    for row in board:
      for column in row:
        if column == 'X':
          x += 1
        elif column == 'O':
          o += 1
    if(x == o):
      return 'X'
    else:
      return 'O'

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    freeSquares = set()
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] is None:
          freeSquares.add((i,j))
          
    return freeSquares
    raise NotImplementedError


def result(board, action):

    copyBoard = copy.deepcopy(board)  
    if action in actions(copyBoard):
      copyBoard[action[0]][action[1]] = player(copyBoard)
      
    return copyBoard
  
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in winnerMoves:
      if board[row[0][0]][row[0][1]] == board[row[1][0]][row[1][1]] == board[row[2][0]][row[2][1]] and board[row[0][0]][row[0][1]] is not None:
        return board[row[0][0]][row[0][1]]

    return None
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
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
