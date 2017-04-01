#!/usr/bin/python


class Node(object):
    """ Graph Node """
    def __init__(self, data):
        self.data = data
        self.children = []

    def addNeighbour(self, data):
        if type(data) == int:
            l = Node(data) 
        else:
            l = data
        self.children.append(l)
        return l 

node = Node(8)
a  = node.addNeighbour(1)
b  = node.addNeighbour(2)
a.addNeighbour(10)
b.addNeighbour(a)
d = b.addNeighbour(14)
a.addNeighbour(21)
d.addNeighbour(44)
e = d.addNeighbour(34)
e.addNeighbour(a)
