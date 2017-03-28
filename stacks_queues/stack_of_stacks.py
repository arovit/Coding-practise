#!/usr/bin/python

from stacks import Node
from stacks import Stack

class OverFlowException(Exception):
    """ Exception for Overflow """ 
    pass

class EmptyStackException(Exception):
    """ Exception for emptyStack """
    pass

class LStack(Stack):
    """ 'Limited stack' derived from stack"""
    def __init__(self, limit):
        self.size = limit 
        self.count = 0
        self.next  = 0
        super(LStack, self).__init__()

    def push(self, node):
        if self.count == self.size:
            raise OverFlowException
        else:
            super(LStack, self).push(node)
            self.count += 1
        
    def pop(self):
        if self.count == 0:
            raise EmptyStackException
        else:
            ele = super(LStack, self).pop()
            self.count -= 1
            return ele

    def __str__(self):
        return "%s ===> %s"%(self.top, self.next)

class StackMaster(object):  ##  new style classes - 'type' same as 'class'
    """ Class to implement stack of stacks with limit on each stack """
    def __init__(self, stack_limit):
        self.stack_size = stack_limit 
        self.top_stack = None
 
    def addItem(self, data):
        node = Node(data)
        self.push(node)

    def pushItemToStack(self, stack, item):
        try:
            stack.push(item) 
        except OverFlowException:
            newstack = LStack(self.stack_size)
            self.pushItemToStack(newstack, item)
            newstack.next = stack
            self.top_stack = newstack

    def push(self, node):
        if self.top_stack:
            self.pushItemToStack(self.top_stack, node)
        else:
            newstack = LStack(self.stack_size)
            self.pushItemToStack(newstack, node)
            self.top_stack = newstack

    def pop(self):
        if not self.top_stack:
            raise EmptyStackException
        try:
            return self.top_stack.pop()
        except EmptyStackException:
            self.top_stack = self.top_stack.next 
            return self.pop()
    
    def printS(self):
        print self.top_stack 


sm = StackMaster(2)
sm.addItem(3)
sm.addItem(4)
sm.addItem(5)
sm.printS()
print sm.pop().data
print sm.pop().data
print sm.pop().data
