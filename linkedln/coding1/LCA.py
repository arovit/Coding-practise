#!/usr/bin/python

from tree import *


def do_inorder(root):
    if root.left:
        do_inorder(root.left)
    print root.data
    if root.right:
        do_inorder(root.right)

"""    
There are two ways to finding LCA - one way is 
1. when parent pointers are given - calculate the height of both the nodes 
if both node have same height , keep traversing up until they both have same parent
if one node is deeper than other, bring up the node which is deeper, and then do above
2. when parent pointers are not given - in that case, make use of BST properties traversing from top to bottom
"""

def find_LCA(root, node1, node2):
    if not root:
        return False
    if root.data > node1.data and root.data > node2.data: ## both are in the left - go left
        return find_LCA(root.left, node1, node2)
    if root.data < node1.data and root.data < node2.data:  ## both are in the right - go right
        return find_LCA(root.right, node1, node2)  
    return root


node1 = root.left.left.left.left 
node2 = root.left.left.left.right.left

lca = find_LCA(root, node1, node2)
print lca.data    



