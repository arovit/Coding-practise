#!/usr/bin/python


## Tic Tac Toe - Checker for winning condition
# |x |x |o |
# |x |x |x |
# |o |o |x |


class TicTacToe(object):
    def __init__(self, size):
        self.boardsize = size
        self.board = [[0]*(size) for i in range(size)]
 
    def winCheck(self):
        for i in range(self.boardsize):
            # Check the ith row
            status, ele = self.checkRow(i)
            print "status %s, row %s"%(status, i)
            if status: return ele 
            status, ele = self.checkColumn(i)
            print "status %s, colunn %s"%(status, i)
            if status: return ele 
        status, ele = self.checkDiagonal()
        if status: return ele
        

    def checkDiagonal(self):
        for i in range(self.boardsize-1):
            if self.board[i][i] == 0 or (self.board[i][i] != self.board[i+1][i+1]):
                return False, None
        return True, self.board[0][0]
                
    def checkRow(self,i):
        for j in range(self.boardsize-1):
            if self.board[i][j] == '0' or (self.board[i][j] != self.board[i][j+1]): # check j columns
                return False, None
        return True, self.board[i][0]

    def checkColumn(self,i):
        for j in range(self.boardsize-1):
            if self.board[j][i] == '0' or (self.board[j][i] != self.board[j+1][i]): # check j columns
                return False, None
        return True, self.board[0][i]


# this is inefficient as all the operations are done again and again. 
# We can perhaps eliminate all the rows which cannot have any winner

class ReTicTacToe(TicTacToe):
    def __init__(self, size):
        super(self, ReTicTacToe).__init__(size)
        self.rows_check_only = {}
        self.column_check_only = {}
        for i in range(self.boardsize): self.rows_check_only.update({i:'1'})
        self.column_check_only = {}
        for i in range(self.boardsize): self.column_check_only.update({i:'1'})

    def winCheck(self):
        for i in self.rows_check_only.keys():
            # Check the ith row
            ele_rows = []
            status, ele = self.checkRow(i)
            if not status:
                if status is None:
                    ele_rows.append(i)    
            else: return ele
        for i in ele_rows:
            del self.rows_check_only[i]

        for i in self.column_check_only.keys(): 
            ele_cols = []
            status, ele = self.checkColumn(i)
            if not status:
                if status is None:
                    ele_cols.append(i)    
            else: return ele
        for i in ele_cols:
            del self.column_check_only[i]

        if self.diacheck:
            status, ele = self.checkDiagonal()
            if not status:
                if status is None:
                    self.diacheck = False    
            else: return ele
 
        return False, None

    def checkRow(self,i):
        for j in range(self.boardsize-1):
            if (self.board[i][j] != self.board[i][j+1]): # check j columns
                return None, None
            if self.board[i][j] == '0':
                return False, None
        return True, self.board[i][0]

    def checkColumn(self,i):
        for j in range(self.boardsize-1):
            if (self.board[j][i] != self.board[j+1][i]): # check j columns
                return None, None
            if self.board[j][i] == '0':
                return False, None 
        return True, self.board[0][i]

    def checkDiagonal(self):
        for i in range(self.boardsize-1):
            if (self.board[i][i] != self.board[i+1][i+1]):
                return None, None
            if self.board[i][i] == '0':
                return False, None 
        return True, self.board[0][0]
    
    
tc = TicTacToe(3)
tc.board = [['x','x','0'],['x','x','x'],['0','0','x']]
print tc.winCheck() 
