#!/usr/bin/python

from trees import Node

n = Node(10)
l1 = n.addleft(2)
r1 = n.addright(20)
l2 = l1.addleft(13)
l3 = l2.addleft(13)
lr2 = l3.addright(19)



def check_balanced_tree(node):
    if not node:
        return 0, True
    lheight, lbalanced = check_balanced_tree(node.left)
    rheight, rbalanced = check_balanced_tree(node.right)
    cheight = max(lheight, rheight) + 1
    if (abs(lheight - rheight) > 2) or (not (lbalanced and rbalanced)):
        balanced = False
    else:
        balanced = True 
    return cheight, balanced


h, b = check_balanced_tree(n)
print "height %s, balanced %s"%(h, b)

