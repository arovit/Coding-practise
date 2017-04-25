#!/usr/bin/python

import copy 

board_size = 8 
board = []
board = [[0 for i in range(board_size)] for j in range(board_size)]


def eight_queen(index, board, plist):
    if index == board_size:
        return True
    newboard = copy.deepcopy(board)
    for i in range(board_size):
        for j in range(board_size):
            if newboard[i][j] == 0:  ## position available
                plist[index]=(i,j)
                newboardpos = copy.deepcopy(newboard)
                cancelpositions(newboardpos, i, j)
                if eight_queen(index+1, newboardpos, plist):
                    return True
                
    return False      

def cancelpositions(board, x, y):
    for i in range(board_size):
        board[i][y] = 1
        board[x][i] = 1
        if 0 <= x+i < board_size:
            if 0 <= y+i < board_size:  
                board[x+i][y+i] = 1
            if 0 <= y-i < board_size:  
                board[x+i][y-i] = 1
        if 0 <= x-i < board_size:
            if 0 <= y+i < board_size:  
                board[x-i][y+i] = 1
            if 0 <= y-i < board_size:  
                board[x-i][y-i] = 1

queen_positions = [(),(),(),(),(),(),(),()]
eight_queen(0, board, queen_positions)
print queen_positions
