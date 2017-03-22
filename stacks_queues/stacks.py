#!/usr/bin/python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return "Data %s -> %s"%(self.data, self.next)

class Stack(object):
    """ Stack implementation """
    def __init__(self):
        self.top = None 

    def addItem(self, data):
        """ Push data onto stack """
        node = Node(data)
        self.push(node)
  
    def push(self, node):
        """ push the top of stack """ 
        if self.top:
            node.next = self.top 
            self.top = node 
        else:
            self.top = node

    def pop(self):
        """ Pop the top of stack """ 
        if self.top:
            temp = self.top
            self.top = self.top.next
            return temp
        else:
            return "Cannot pop"  ## Some exception
          
    def peek(self):
        """ Peek the top of stack """ 
        if self.top:
            return self.top.data
        else:
            return "Cannot seek"

    def printStack(self): 
        """ Print Stack """
        print self.top
        

"""s1 = Stack()
s1.addItem("1")
s1.addItem("8")
s1.addItem("3")
s1.addItem("5")
s1.printStack()
s1.pop()
s1.printStack()
s1.pop()
s1.printStack()
s1.pop()
s1.printStack()"""
