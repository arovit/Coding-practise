#!/usr/bin/python


# remove generate leaf nodes

from tree import *

def falling_leaves(node, flist):
    if not node.left and not node.right:
        flist.append(node.data)
        return 1

    if node.left:
        status = falling_leaves(node.left, flist)
        if status:
           node.left = None
    if node.right:
        status = falling_leaves(node.right, flist)
        if status:
           node.right = None

root = Node('K')
root.left = Node('G')
root.right = Node('Q')

root.left.left = Node('C')
root.left.right = Node('H')
        
root.right.left = Node('M')
root.right.right = Node('Y')

root.left.left.left = Node('B')
root.left.left.right = Node('D')

root.right.left.right = Node('P')

flist = []
falling_leaves(root, flist)
print flist
    
