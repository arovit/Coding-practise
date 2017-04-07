#!/usr/bin/python

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None 
        self.size = 1
        self.parent = None  ## may or may not be true
      
    def addleft(self, data):
        node = Node(data)
        self.left = node 
        node.parent = self
        self.increase_size(node)
        return self.left

    def increase_size(self, node):
        while node.parent:
            node.parent.size += 1
            node = node.parent 
             
    def addright(self, data):
        node = Node(data)
        self.right = node 
        node.parent = self
        self.increase_size(node)
        return self.right

    def __str__(self, level=0):
        ret = "-"*level+repr(self.data)+"\n"
        for child in [self.left, self.right]:
            if child:
                ret += child.__str__(level+1)
        return ret

def in_order(node):
    if node:
        in_order(node.left)
        print node.data
        in_order(node.right)

def pre_order(node):
    if node:
        print node.data
        pre_order(node.left)       
        pre_order(node.right)       

def post_order(node):
    if node:
        post_order(node.left)       
        post_order(node.right)       
        print node.data

"""        
n = Node(10)
l1 = n.addleft(2)
r1 = n.addright(20)
l2 = l1.addleft(13)
lr2 = l1.addright(19)
print "In order"
in_order(n)
print "Pre order"
pre_order(n)
print "Post order"
post_order(n)
"""
