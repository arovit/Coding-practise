#!/usr/bin/python

import sys
# Practising top 5 questions

#1. Reverse a string

def reverse_string(given_str):
    given_str = list(given_str)
    tlen = len(given_str)    
    for i in range(0, tlen/2):
        given_str[i], given_str[tlen-1-i] = given_str[tlen-1-i], given_str[i]
    print "".join(given_str)    

#reverse_string("arovi")

def fibonacci_number(n):
    return n if n <= 1 else fibonacci_number(n-1) + fibonacci_number(n-2)

assert 1 == fibonacci_number(1)
assert 1 == fibonacci_number(2)
assert 2 == fibonacci_number(3)

def grade_school_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            sys.stdout.write("%4d "%(i*j))
        sys.stdout.write("\n")

#grade_school_table(12)


def print_odd_number(n):
    for i in range(1,n+1):
        if i & 1:
            print i

#print_odd_number(20) 

class Tree(object):
    """ Tree Node Implementation """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 

def inorder_traversal(n):
    """ In order traversal O(n) """
    if n:
        if n.left: 
            inorder_traversal(n.left) 
        print n.data
        if n.right:
            inorder_traversal(n.right) 


def preorder_traversal(n):
    """ Preorder traversal O(n) """
    if n:
        print n.data
        if n.left:
            preorder_traversal(n.left)
        if n.right:
            preorder_traversal(n.right)
      
def postorder_traversal(n):
    """ Preorder traversal O(n) """
    if n:
        if n.left:
            postorder_traversal(n.left)
        if n.right:
            postorder_traversal(n.right)
        print n.data


def DFS(n):
    if not n: return
    print n.data
    for i in [n.left, n.right]:
        DFS(i)

def BFS(n):
    queue = []
    queue.append(n)
    while queue:
       current_node = queue.pop(0)
       if current_node.left:queue.append(current_node.left)
       if current_node.right: queue.append(current_node.right)
       print current_node.data

def check_balance(node):
    lheight = rheight = 0
    lstatus = rstatus = True
    if node.left: lheight, lstatus = check_balance(node.left) 
    if node.right: rheight, rstatus = check_balance(node.right) 
    return max(lheight+1, rheight+1), ((lstatus or rstatus) and abs(rheight-lheight) <= 2) 

root = Tree(34)   
root.left=Tree(24)
root.right=Tree(44)
root.left.left=Tree(14)
root.left.right=Tree(30)
root.left.left.left=Tree(10)
root.left.left.left.left=Tree(5)
root.left.left.left.left.left=Tree(3)


#inorder_traversal(root)
#print "-"*10
#preorder_traversal(root)
#print "-"*10
#postorder_traversal(root)
#print "-"*10
#BFS(root)
#print "-"*10
#DFS(root)
print check_balance(root)
