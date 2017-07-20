#!/usr/bin/python

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.totalResult = []
        self.solvedPos = []
        q_pos = [-1 for i in range(n)]
        index = 0
        self.solve(q_pos, index)
        self.formAnswer(n)
        return self.solvedPos
        
    def formAnswer(self, n):
        for i in self.totalResult: # element of len - list
            result = []
            for k in range(len(i)):       # i is a list
                ostr = ['.']*n
                ostr[i[k]] = 'Q'
                result.append(''.join(ostr))
            self.solvedPos.append(result)
            
    def solve(self, q_pos, index):
        if index == len(q_pos):
            self.totalResult.append(copy.deepcopy(q_pos))
            return 
        for i in range(len(q_pos)):
            q_pos[index] = i
            if self.validatePos(q_pos, index):
                self.solve(q_pos, index+1)
        
    def validatePos(self, q_pos, index):
        for i in range(index):
            if (q_pos[i] == q_pos[index]) or (index-i == abs(q_pos[i]-q_pos[index])):
                return False
        return True

sol = Solution()
sol.solveNQueens(6)
print sol.solutions.values()
