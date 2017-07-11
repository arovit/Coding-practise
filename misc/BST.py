#!/usr/bin/python


class Node(object):
    def __init__(self, data):
        self.val  = data
        self.left = None    
        self.right = None


def search(value, node):
    if (not node) or (node.val == value):
        return node
    return search(value, node.left) if node.val > value else search(value, node.right)


def insert(node, newnode):
    if node.val > newnode.val: # new node is lesso 
        if not node.left:
            node.left = newnode
        else:
            insert(node.left, newnode)
    else: # new node is moreo
        if not node.right:
            node.right = newnode 
        else:
            insert(node.right, newnode)


def inorder(root):
    if root.left:
        inorder(root.left)
    print root.val
    if root.right:
        inorder(root.right)


root = Node(50)
root.left = Node(25)
root.right = Node(75)
root.left.right = Node(35)
newnode = Node(15)
insert(root, newnode)

inorder(root)

node = search(15, root)
if node:
    print "search found a node"
else:
    print "search unsuccessful"
