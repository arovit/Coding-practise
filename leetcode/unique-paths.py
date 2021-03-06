#!/usr/bin/python


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        pathGrid = [[0 for j in range(n)] for i in range(m)] 
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0):
                    pathGrid[i][j] = 1
                    continue
                fromUp =  0 if i-1 < 0 else pathGrid[i-1][j]
                fromLeft = 0 if j-1 < 0 else pathGrid[i][j-1] 
                pathGrid[i][j] = fromUp + fromLeft
        print pathGrid[m-1][n-1] 



sol = Solution()
# 1 1 1 
# 1 2 3 
# 1 3 6 
sol.uniquePaths(3,3)
