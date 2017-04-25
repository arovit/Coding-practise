#!/usr/bin/python

import copy

def solve(board):
    newboard = copy.deepcopy(board)
    returndata = get_data(newboard)
    if returndata == False:
        return False
    else:
        row_hash, col_hash, quad_hash = returndata[0], returndata[1], returndata[2]
    #print newboard
    if boardisfull(newboard):
        return True
    sorted_rows = sorted(row_hash.items(), key=lambda x:len(x[1]))
    sorted_cols = sorted(col_hash.items(), key=lambda x:len(x[1]))
    sorted_quads = sorted(quad_hash.items(), key=lambda x:len(x[1]))
    for i in sorted_rows:
        for j in sorted_cols:
            x = i[0]
            y = j[0]
            found = 0
            qrow, qcol = get_quad(x, y)
            if newboard[x][y] == ".":
                for num in range(1, 10):
                    if not ((num in row_hash[x]) or (num in col_hash[y]) or (num in quad_hash[(qrow,qcol)])):
                        newboard[x][y] = num 
                        if solve(newboard):
                            return True
                        newboard[x][y] = "."
    return False             
                             
def boardisfull(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return False
    return True
                                  
def get_quad(x,y):
    if y <= 2:
        qcol = 2
    elif y <=5:
        qcol = 5
    else:
        qcol = 8
    if x <= 2:
        qrow = 2
    elif x <=5:
        qrow = 5
    else:
        qrow = 8
    return qrow, qcol

def get_data(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    row = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
    column = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
    quad_hash = {(2,2):{}, (2,5):{}, (2,8):{},
                     (5,2):{}, (5,5):{}, (5,8):{},
                     (8,2):{}, (8,5):{}, (8,8):{}}
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            if board[i][j] in row[i]:
                return False
            else:
                row[i].update({board[i][j]:1})
            if board[i][j] in column[j]:
                return False
            else:
                column[j].update({board[i][j]:1})
            qrow , qcol = get_quad(i,j)
            if board[i][j] in quad_hash[(qrow,qcol)]:
                return False
            else:
                quad_hash[(qrow, qcol)].update({board[i][j]:1})
    return row, column, quad_hash


def chartest(x):
    if x == ".":
        return x
    else:
        return int(x)
sudo = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
#sudo = [".19748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
sudo = [map(chartest, list(i)) for i in sudo]
solve(sudo)
