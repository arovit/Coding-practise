#!/usr/bin/python

import trees
def same_tree(node1, node2):
    if node1 == None and node2 == None:
        return True
    if (node1 == None and node2 != None) or (node2 == None and node1 != None):
        return False
    if node1.data == node2.data:
        return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right) 
    else:
        return False    



def check_subtree(root1, root2):
    if same_tree(root1, root2):
        return True
    if not root1:
        return False
    return check_subtree(root1.left,root2) or check_subtree(root1.right, root2) 



n1 = trees.Node(10)
a = n1.addleft(5)
b = n1.addright(8)
a.addleft(1)
b.addleft(2)

n2 = trees.Node(8)
n2.addleft(3)


print check_subtree(n1, n2)
