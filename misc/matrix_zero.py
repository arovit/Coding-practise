#!/usr/bin/python


# Problem: Assign zero to rows and columns if element = 0 

matrix = [[1,2,0], [4,0,6], [7,8,1]]
zero_rows = set()
zero_columns = set() 

for i in range(len(matrix)):
    for j in range(len(matrix)): 
        if matrix[i][j] == 0:
            zero_rows.add(i) 
            zero_columns.add(j)

for i in zero_rows:
    for j in range(len(matrix)):
        matrix[i][j] = 0


for i in zero_columns:
    for j in range(len(matrix)):
        matrix[j][i] = 0     

print matrix
