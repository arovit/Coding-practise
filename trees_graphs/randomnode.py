#!/usr/bin/python

import trees
import random

a = trees.Node(50)

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


def get_random_node(a):
    """ Get random nodes """
    if not a.left: 
        lc = 0
    else:
        lc = a.left.size
    index = random.randint(1, a.size)
    if index == lc+1:
        return a.data
    elif index <= lc:
        return get_random_node(a.left)
    else:
        return get_random_node(a.right)    
    

print get_random_node(a)
