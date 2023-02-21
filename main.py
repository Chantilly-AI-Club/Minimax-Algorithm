import copy
import math
from ticTacToe import TicTacToe
board = [['','',''],
         ['','',''],
         ['','','']]

def match():
    state = 'X'
    tictactoe = TicTacToe(board)
    while not tictactoe.checkWinState():
        tictactoe.display_board()
        print('Enter row number')
        row = int(input())
        print('Enter column number')
        column = int(input())
        
        tictactoe.update_move(row,column,'X')
        AI = best_move(tictactoe.get_board())
        tictactoe.update_move(AI[0],AI[1],'O')

    tictactoe.display_board()
    print(state + " has lost")

def best_move(board):
    bestScore= math.inf
    bestMove = None
    actual_board = TicTacToe(board)
    for move in actual_board.get_available_moves():
        copyBoard = copy.deepcopy(actual_board)
        copyBoard.update_move(move[0],move[1],'O')
        score = minimax('X',copyBoard.get_board())
        if(score < bestScore):
            bestScore = score
            bestMove = move
        copyBoard = board
    return bestMove

def minimax(maximizing, board):
    actual_board = TicTacToe(board)
    if(actual_board.get_available_moves() == [] and not actual_board.checkWinState()):
        return 0
    if(actual_board.checkWinState() and actual_board.get_last_move() == 'X'):
        return 1
    if(actual_board.checkWinState() and actual_board.get_last_move() == 'O'):
        return -1

    scores = []
    for move in actual_board.get_available_moves():
        copyBoard = copy.deepcopy(actual_board)
        copyBoard.update_move(move[0],move[1],copyBoard.get_next_turn())
        scores.append(minimax(copyBoard.get_next_turn(), copyBoard.get_board()))
        copyBoard = actual_board    

    return max(scores) if maximizing == 'X' else min(scores)


if __name__ == "__main__":
    match()
  