#!/usr/bin/python

class Solution(object):
    def totalNQueens(self, n):
        self.total_res = 0
        self.dfs([-1 for i in range(n)], 0) 
        return self.total_res

    def dfs(self, qlist, index):
        print qlist
        if index == len(qlist):
            self.total_res += 1
            return 
        for i in range(len(qlist)):
            qlist[index] = i
            if self.validate(qlist, index):
                self.dfs(qlist, index+1)

    def validate(self, qlist, index):
        for i in range(index):
            if (qlist[i] == qlist[index]) or (abs(qlist[index]-qlist[i]) == index-i):
                return False
        return True


sol = Solution()
print sol.totalNQueens(4)



