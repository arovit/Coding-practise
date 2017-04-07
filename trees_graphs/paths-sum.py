#!/usr/bin/python

import trees

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

def doBFS(root, targetsum):
    qu = [] 
    qu.append(root)
    while qu: 
        node = qu.pop(0)
        checksum(node, '', 0, targetsum)
        if node.left:
            qu.append(node.left)
        elif node.right:
            qu.append(node.right) 
      
def checksum(node, path, tsum, target):
    """ Check sum """
    if node:
        path = path + "->%s"%node.data
        tsum = tsum + node.data
        if tsum == target:
            print path
            return 
        if node.left:
            checksum(node.left, path, tsum, target)
        if node.right:
            checksum(node.right, path, tsum, target)
    return         


doBFS(a, 40)
