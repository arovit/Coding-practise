#!/usr/bin/python

## Problem : Rotate the matrix by 90 degress

matrix = [[1,2,3], [4,5,6], [7,8,9]]
new_matrix = []
for i in range(len(matrix)):
    temp = []
    for j in range(len(matrix)-1,-1,-1): 
       temp.append(matrix[j][i]) 
    new_matrix.append(temp)

print new_matrix
