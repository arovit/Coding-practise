#!/usr/bin/python

import trees

def FCA(node1, node2):
    """ find the first common ancestor """
    h1 = depth(node1)
    h2 = depth(node2)
    if h1 != h2:
        if h1 < h2:
            node2 = travel_up(node2, h2, h1)
        else:
            node1 = travel_up(node1, h1, h2)

    if node1 == node2: ##  if both are same nodes
        return node1

    while True:
        if node1.parent != node2.parent:
            node1 = node1.parent
            node2 = node2.parent 
        else:
            return node1.parent 

def travel_up(deeper, start, end):
    while start != end:
        start = start - 1 
        deeper = deeper.parent
    return deeper

def depth(node):
    depth = 0
    while True:
        if node.parent:
            depth = depth + 1
            node = node.parent
        else: 
            break
    return depth

def input_tree():
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
    return a, b,i 


root, node1, node2  = input_tree()
node = FCA(node1, node2)
print node.data
