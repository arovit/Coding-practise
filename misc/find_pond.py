#!/usr/bin/python

#  1 2 3 0
#  0 1 2 0
#  0 0 1 1
#  0 3 0 0

def findAllPondSizes(land):
    rows = len(land)
    col  = len(land[0]) 
    for i in range(rows):
        for j in range(col):
            if land[i][j] == 0:
                print computePondSize(i,j,land) 



def computePondSize(r,c,land):
    if r < 0 or c < 0 or r >= len(land) or c >= len(land[0]) or land[r][c] != 0:
        return 0 
    sum = 1 
    land[r][c] = -1  # mark visited
    for i in [-1,0,1]:
        for j in [-1,0,1]: 
            sum += computePondSize(r+i, c+j, land)
    return sum

land = [[1,2,3,0],[0,1,2,0],[0,0,1,1],[0,2,0,0]]
findAllPondSizes(land)
