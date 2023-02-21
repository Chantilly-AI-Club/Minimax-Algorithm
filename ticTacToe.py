class TicTacToe:
    def __init__(self,board):
        self.board = board

    def display_board(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print()

    def get_board(self):
        return self.board
    
    def get_available_moves(self):
        available_moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(self.board[row][col] == ''):
                    available_moves.append((row,col))
        return available_moves

            
    
    def update_move(self, row, column, move):
        if((self.board[row][column] == '') and (move == 'O' or move == 'X')):
            self.board[row][column] = move
        else:
            raise Exception("Inputs must be 'X' or 'O' and you cannot replace moves made")
    
    def get_last_move(self):
        x_count = 0
        o_count = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 'X': x_count+=1
                if self.board[row][col] == 'O': o_count+=1
        if x_count == o_count:
            return 'O'
        else:
            return 'X'

    def checkWinState(self):
        #if in a row in a column, or in diagonal
        winState = False
        if( (self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X') or (self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O')): winState = True
        if( (self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X') or (self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O')): winState = True
        if( (self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X') or (self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O')): winState = True
        
        if( (self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X') or (self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O')): winState = True
        if( (self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X') or (self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O')): winState = True
        if( (self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X') or (self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O')): winState = True
    
        if( (self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X') or (self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O')): winState = True
        if( (self.board[2][0] == 'X' and self.board[1][1] == 'X' and self.board[0][2] == 'X') or (self.board[2][0] == 'O' and self.board[1][1] == 'O' and self.board[0][2] == 'O')): winState = True
        return winState
    

    def get_next_turn(self):
        x_count = 0
        o_count = 0
        ret_val = ''
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 'X': x_count+=1
                if self.board[row][col] == 'O': o_count+=1
        if x_count == o_count:
            ret_val = 'X'
        if x_count > o_count:
            ret_val = 'O'
        return ret_val      