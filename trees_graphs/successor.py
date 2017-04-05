#!/usr/bin/python

import trees

def get_successor(node):
    """ Get successor of a node in binary search tree """
    if node.right:
        snode = leftmost(node.right)
    else:
        snode = parent_until_greator(node, node.data)
    return snode.data
         

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

print a = trees.Node(50)

b = a.addleft(48)
i = a.addright(52)

c = b.addleft(25)

d = c.addleft(10)
f = c.addright(30)

e = d.addleft(5)

g = f.addleft(28)
h = f.addright(32)

j = i.addleft(51)
k = i.addright(54)


print get_successor(c)
