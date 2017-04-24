#!/usr/bin/python

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
	row = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        column = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        quad_hash = {(2,2):{}, (2,5):{}, (2,8):{}, 
                     (5,2):{}, (5,5):{}, (5,8):{},
                     (8,2):{}, (8,5):{}, (8,8):{}} 
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue 
                if board[i][j] in row[i]:
                    return False
                else:
                    row[i].update({board[i][j]:1})
                if board[i][j] in column[j]:
                    return False
                else:
                    column[j].update({board[i][j]:1})
                if j <= 2:
                    qcol = 2   
                elif j <=5:
                    qcol = 5
                else:
                    qcol = 8  
                if i <= 2:
                    qrow = 2
                elif i <=5:
                    qrow = 5
                else:
                    qrow = 8
                if board[i][j] in quad_hash[(qrow,qcol)]:
                    return False
                else:
                    quad_hash[(qrow, qcol)].update({board[i][j]:1})
        print "row:",row
        print "column:",column
        print quad_hash 
        return True    

sol = Solution()
print sol.isValidSudoku(["...9.....",".........","..3.....1",".........","1.....3..","....2.6..",".9.....7.","........7","8..8....."])
