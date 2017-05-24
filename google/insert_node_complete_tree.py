#!/usr/bin/python


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertNodeToCompleteTree(node):
    """ Inserts node into a complete tree. 
    If a node has either left or right child free - insert there ( left before right )
    Else, go for left most node in the last level """ 
    nodeQueue = []
    nodeQueue.append(node)
    while nodeQueue:
        node = nodeQueue.pop(0)
        if node.left and node.right:
            nodeQueue.append(node.left)
            nodeQueue.append(node.right)
        elif node.left and not node.right:
            ## insert at node.right
            node.right = Node('inserted')
            return
        elif node.right and not node.left:
            ## insert at the node.left
            node.left = Node('inserted')
            return
        else:
            # insrt at node.left
            node.left = Node('inserted')
            return
            

root = Node(3)
root.left = Node(2)
root.right = Node(5)
insertNodeToCompleteTree(root) 
print root.left.left.data
