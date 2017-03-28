#!/usr/bin/python

from stacks import Node
from stacks import Stack

class SortStack(Stack):   ## Stack that has capability to sort itself
    """ Stack with Sort implementation """
    def __init__(self):
        super(SortStack, self).__init__()     
        

    def sortStack(self):
        tempStack = Stack()  ## use of temp stack allowed 
        tempEle = None
        while True:
            if tempEle is None:
                tempEle = self.pop()
            compareEle = self.pop()
            if type(compareEle) == str:
                break
            if tempEle < compareEle:
                tempStack.push(tempEle)
                tempEle = compareEle
            else:
                tempStack.push(compareEle)
        self.push(tempEle) 
        while True:
            ele = tempStack.pop()
            if type(ele) == str: 
                break
            else:
                self.push(ele)  

    def sort(self):
        stacksize = 10
        for i in range(stacksize):
            self.sortStack() 
        self.printStack()

s = SortStack()
s.addItem(21)
s.addItem(13)
s.addItem(23)
s.addItem(51)
s.addItem(16)
s.addItem(61)
s.addItem(36)
s.addItem(76)
s.sort()
