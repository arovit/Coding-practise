#!/usr/bin/python

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) > len(board) * len(board[0]):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.seeNeighbours(i,j,word[1:], board, [(i,j)]):
                        return True
        return False
        
        
    def seeNeighbours(self, row, col, word, board, seen):
        if not word:
            return True
        if (row == len(board)) or (row < 0) or (col == len(board[0])) or (col < 0):
            return False
        mstatus = False
        if (col-1 >= 0) and board[row][col-1] == word[0] and (row, col-1) not in seen:
                seen.append((row,col-1))
                mstatus = self.seeNeighbours(row, col-1, word[1:], board, seen)
                if not mstatus:
                    seen.pop()
        if (col+1 < len(board[0])) and board[row][col+1] == word[0] and (not mstatus) and (row, col+1) not in seen:
                seen.append((row,col+1))
                mstatus = self.seeNeighbours(row, col+1, word[1:], board, seen)
                if not mstatus:
                    seen.pop()
        if (row-1 >= 0) and board[row-1][col] == word[0] and (not mstatus) and (row-1, col) not in seen:
                seen.append((row-1,col))
                mstatus = self.seeNeighbours(row-1, col, word[1:], board, seen)
                if not mstatus:
                    seen.pop()
        if (row+1 < len(board)) and board[row+1][col] == word[0] and (not mstatus) and (row+1, col) not in seen:
                seen.append((row+1,col))
                mstatus = self.seeNeighbours(row+1, col, word[1:], board, seen)
                if not mstatus:
                    seen.pop()
        return mstatus

sol = Solution()
print sol.exist(['aab'],'aaa')


