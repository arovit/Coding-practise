#!/usr/bin/python


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                left = grid[i][j-1] if j-1 >= 0 else -1
                up  = grid[i-1][j] if i-1 >= 0 else -1
                newsum = 0
                if left >= 0 and up >= 0:
                    newsum = min(left, up)
                elif left == -1 and up == -1:
                    newsum = 0
                else:
                    newsum = up if left == -1 else left
                grid[i][j] = newsum + grid[i][j]
        return grid[m-1][n-1] 
