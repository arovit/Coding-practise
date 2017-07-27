#!/usr/bin/python

class Node(object):
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

root = Node(100)
root.left = Node(50)
root.right = Node(150)

root.left.left = Node(32)
root.left.right = Node(59)

root.left.left.left = Node(20)
root.left.right.right = Node(65)

root.left.left.left.left = Node(10)
root.left.left.left.right = Node(28)
root.left.right.right.left = Node(62)
root.left.left.left.right.left = Node(25)

def BFS(root):
    queue = []    
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print node.data
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#BFS(root)
