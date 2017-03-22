#!/usr/bin/python


""" Program to have a stack with O(1) push, O(1) pop, O(1) min op """
from stacks import  *

class NewStack(Stack):
    def __init__(self):
        super(NewStack, self).__init__()

    def push(self, node):
        if self.top:
            lmin = self.top.min 
        else:
            lmin = 9999999999999
        super(NewStack, self).push(node)
        if self.top.data < lmin:
            self.top.min = self.top.data
        else:
            self.top.min = lmin
     
    def min(self):
        return self.top.min

ns = NewStack()
ns.addItem(98)
ns.addItem(43)
ns.addItem(3)
ns.addItem(8)
ns.addItem(7)
ns.addItem(9)
ns.addItem(1)
ns.printStack() 
print ns.min()
ns.pop()
ns.printStack() 
print ns.min()
ns.pop()
ns.printStack() 
print ns.min()
ns.pop()
ns.printStack() 
print ns.min()
ns.pop()
ns.printStack() 
print ns.min()
ns.pop()
ns.printStack() 
print ns.min()
