#!/usr/bin/python


def get_successor(node):
    """ Get successor of a node in binary search tree """
    if node.right:
        lnode = leftmost(node.right)
    else:
        pnode = parent_until_greator(node, node.data)
         

def leftmost(node):
    if node.left:
        return leftmost(node.left) 
    else:
        return node


def parent_until_greator(node, val):
    if not node:
        return None

    if node.data > val: 
        return node
    else:
        return parent_until_greator(node.parent, val)   
