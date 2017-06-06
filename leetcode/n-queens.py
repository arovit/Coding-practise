#!/usr/bin/python

import copy

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.solutions = {}
        board = [['0' for i in range(n)] for i in range(n)]
        self.solve_n_queens(n, 0, board)
      
    def solve_n_queens(self, n , count, board):
        if count == n:
            result = copy.deepcopy(board)
            key = "%s"%(result) 
            result = [''.join(x) for x in result]
            if key not in self.solutions: 
                self.solutions.update({key:result})
            return 
        for row in range(n):
            for col in range(n):
                if board[row][col] == '0':
                    newboard = copy.deepcopy(board)
                    self.cancel_positions(row, col, n, newboard)
       
    def cancel_positions(self, row, col, n, board): 
        for i in range(n):
            board[row][i] = '.'
            board[i][col] = '.'  
            if row+i < n and col+i < n : board[row+i][col+i] = '.' 
            if row+i < n and col-i >= 0: board[row+i][col-i] = '.'
            if row-i >= 0 and col+i < n: board[row-i][col+i] = '.'
            if row-i >= 0 and col-i >=0: board[row-i][col-i] = '.'
            board[row][col] = 'Q'


sol = Solution()
sol.solveNQueens(6)
print sol.solutions.values()
