#!/usr/bin/python

# gets number of elements less than equal to that element

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.leftsize = 0

    def addnode(self, data):
        if data > self.data:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.addnode(data)
        else: # dat <= self.data
            self.leftsize += 1
            if data != self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.addnode(data) 
                
    def getrank(self, data):
        if data == self.data: 
            return self.leftsize
        elif data > self.data:
            return self.leftsize + 1 + self.right.getrank(data)
        elif data < self.data:
            return self.left.getrank(data)

def rank_of_number(numlist):
    head = None 
    for i in numlist:
        if not head:
            head = Node(i)
        else:
            head.addnode(i)     
    print head.getrank(4) 

rank_of_number([5,1,2,3,4,6,3,4,8,9])
