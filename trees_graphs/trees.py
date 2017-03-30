#!/usr/bin/python

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None 
        
    def addleft(self, data):
        node = Node(data)
        self.left = node 
        return self.left

    def addright(self, data):
        node = Node(data)
        self.right = node 
        return self.right


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
