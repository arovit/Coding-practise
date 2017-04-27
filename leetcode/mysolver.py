#!/usr/bin/python


def solve(array):
    found = False
    for i in range(9):
        for j in range(9):
            if array[i][j] == ".":
                found = True
                for num in range(1,10):
                    if safe(num, i, j, array):
                        array[i][j] = num
                        if solve(array): 
                            return True 
                        array[i][j] = "."
    if not found:
        return True
     
def safe(num, x, y, array):
    for i in range(9):
        if array[x][i] == num:
            return False
        elif array[i][y] == num:
            return False 
    xbox = x - (x%3)     
    ybox = y - (y%3)
    for i in range(3):
        for j in range(3):
            if array[xbox+i][ybox+j] == num:
                return False
    return True


def chartest(x):
    if x == ".":
        return x
    else:
        return int(x)

sudo = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
#sudo = [".19748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
sudo = [map(chartest, list(i)) for i in sudo]
solve(sudo)
