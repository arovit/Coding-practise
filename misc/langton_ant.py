#!/usr/bin/python

import sys

class Ant(object):
    def __init__(self):
        self.orientation = "right"
        self.positionx = 0
        self.positiony = 0

    def moveAntiClock(self):
        if self.orientation == "left":
            self.orientation = "down"
            self.positionx += 1 
        elif self.orientation == "down":
            self.orientation = "right"
            self.positiony += 1 
        elif self.orientation == "right":
            self.orientation = "up"
            self.positionx -= 1 
        elif self.orientation == "up":
            self.orientation = "left"
            self.positiony -= 1 
         
    def moveClock(self):
        if self.orientation == "left":
            self.orientation = "up"
            self.positionx -= 1 
        elif self.orientation == "down":
            self.orientation = "left"
            self.positiony -= 1 
        elif self.orientation == "right":
            self.orientation = "down"
            self.positionx += 1 
        elif self.orientation == "up":
            self.orientation = "right"
            self.positiony += 1 

    def __repr__(self):
        return "(%s, %s, %s)"%(self.positionx, self.positiony, self.orientation)
         
class Grid(object):
    def __init__(self):
        self.__grid = [[1 for i in range(1)]for i in range(1)] # 1 is white
        self.__ant = Ant()

    def copyWithShift(self, oldGrid, newGrid, shiftRow, shiftColumn):
        for i in range(len(oldGrid)):
            for j in range(len(oldGrid[0])):
                newGrid[shiftRow+i][shiftColumn+j] = oldGrid[i][j]
                 
    def expandGrid(self, newposx, newposy):
        createNewGrid = False
        numRows = len(self.__grid)
        numCols = len(self.__grid[0])
        shiftRow = 0
        shiftColumn = 0
        if newposx >= len(self.__grid):
            numRows = 2*(len(self.__grid))      
            createNewGrid = True
        elif newposx < 0:
            numRows = 2*(len(self.__grid))      
            shiftRow = len(self.__grid)
            createNewGrid = True
        if newposy >= len(self.__grid[0]):
            numCols = 2*(len(self.__grid[0]))
            createNewGrid = True
        elif newposy < 0:
            numCols = 2*(len(self.__grid[0]))
            shiftColumn = len(self.__grid[0])
            createNewGrid = True
        if createNewGrid:
            temparray = [[1 for i in range(numCols)] for j in range(numRows)] 
            self.copyWithShift(self.__grid, temparray, shiftRow, shiftColumn) 
            self.__grid = temparray
        self.__ant.positionx += shiftRow
        self.__ant.positiony += shiftColumn 

    def moveAnt(self):
        if self.__grid[self.__ant.positionx][self.__ant.positiony] == 1: # white 
            self.__grid[self.__ant.positionx][self.__ant.positiony] = 0  # flip it 
            self.__ant.moveClock()
        else:
            self.__grid[self.__ant.positionx][self.__ant.positiony] = 1  # flip it 
            self.__ant.moveAntiClock()
        self.expandGrid(self.__ant.positionx, self.__ant.positiony)

    def printGrid(self):
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[0])):
                sys.stdout.write("%s "%self.__grid[i][j])
            sys.stdout.write("\n")
        print self.__ant

grid = Grid()
grid.moveAnt()
grid.moveAnt()
grid.moveAnt()
grid.moveAnt()
grid.moveAnt()
grid.moveAnt()
grid.moveAnt()
grid.moveAnt()
grid.moveAnt()
grid.printGrid()
