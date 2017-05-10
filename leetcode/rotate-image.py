#!/usr/bin/python


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        total_row = len(matrix)
        total_col = len(matrix[0]) 
        middle = len(matrix)//2 
        for i in range(middle):
            matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]
        col = 0
        for i in range(total_row):
            for j in range(col,total_col):
                print i,j
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  
            col += 1 
        print matrix
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(matrix)
