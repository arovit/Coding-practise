#!/usr/bin/python

# given input cost of coloring, find min cost of coloring the  houses

matrix = [[7,5,10],[3,6,1],[8,7,4],[6,2,9],[1,4,7],[2,3,6]]

def calc_cost(matrix):
    colors = len(matrix[0])
    color_matrix = [[0 for i in range(colors)] for j in range(len(matrix)+1)] 

    for i in range(1,len(matrix)+1):
        color_matrix[i][0] = min(color_matrix[i-1][1], color_matrix[i-1][2]) + matrix[i-1][0]
        color_matrix[i][1] = min(color_matrix[i-1][0], color_matrix[i-1][2]) + matrix[i-1][1]
        color_matrix[i][2] = min(color_matrix[i-1][0], color_matrix[i-1][1]) + matrix[i-1][2]

    print color_matrix[-1] 


calc_cost(matrix)
