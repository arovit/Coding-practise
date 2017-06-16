#!/usr/bin/python


def spiral_matrix(n):
    # initialize
    result = [[0]*n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1  
    for val in range(n*n):
        result[i][j] = val
        nr = (i+di)%n
        nc = (j+dj)%n 
        if result[nr][nc]:  ## if next is already occupied, take right turn  
            di, dj = dj, -di
        i += di
        j += dj  
    return result
 
