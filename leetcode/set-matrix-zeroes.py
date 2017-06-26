#!/usr/bin/python

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows_to_zero = set()
        cols_to_zero = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        for i in range(rows):
            for j in range(cols):
                if (i in rows_to_zero) or (j in cols_to_zero):
                    matrix[i][j] = 0
