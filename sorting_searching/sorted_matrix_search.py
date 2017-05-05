#!/usr/bin/python

def searchElement(matrix, target):
    """ Search through the matrix """
    maxcol = len(matrix[0])-1
    maxrow = len(matrix)-1
    rtype = searchHelper(matrix, 0, maxcol, target, maxcol, maxrow)
    return rtype

def searchHelper(matrix, row, col, target, mcol, mrow):
    """ Search helper """ 
    if (row > mrow):
        return None
    elif (col < 0):
        return 0
    if matrix[row][col] < target:
        return searchHelper(matrix, row+1, col, target, mcol, mrow) 
    elif matrix[row][col] > target:
        return searchHelper(matrix, row, col-1, target, mcol, mrow) 
    else:
        return (row,col) 

matrix = [[1,10,20,40], [3,13,23,41], [6,15, 24, 42], [9,17,27,50]]
print searchElement(matrix, 510)
