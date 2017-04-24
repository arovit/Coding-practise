#!/usr/bin/python

import copy 

board = []
board = [[0 for i in range(8)] for j in range(8)]


def eight_queen(index, board, plist):
    newboard = copy.deepcopy(board) 
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:  ## position available
                plist[index] == (i,j)
                cancel    



def cancelpositions(board, x, y, minx, maxx, miny, maxy):
    for i in range(8):
        board[i][y] = 1    
        board[x][i] = 1
        if minx <= x+i <=maxx:  

        if minx <= x+i <=maxx:  
            board[x+i][y+i] = 1
        board[x+i][y-i] = 1
        board[x-i][y-i] = 1
        board[x-i][y+i] = 1
