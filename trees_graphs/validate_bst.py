#!/usr/bin/python

from trees import *
import sys

def validate_bst(node, min, max):
    if max > node.data > min:
        if node.left:
            lvalidate = validate_bst(node.left, min, node.data)
            if not lvalidate:
                return False
        if node.right:
            rvalidate = validate_bst(node.right, node.data, max)
            if not rvalidate:
                return False
        return True
    else:
        return False    

a = Node(50)

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

min = -1 * sys.maxint      
max = sys.maxint      
print validate_bst(a, min, max) 
