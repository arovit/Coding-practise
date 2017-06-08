#!/usr/bin/python


# factorial
import math

4,3,2,1

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) *n 

assert factorial(3) == 6

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

assert isPrime(5) == True
assert isPrime(6) == False
def permutationGenerate(prefix, string):
    if not string:
        print prefix 
    for i in range(len(string)):
        permutationGenerate(prefix+string[i], string[:i]+string[i+1:]) 
    


print permutationGenerate('','abc')

def combinationsGenerate(string, kcount):  # choose kcount from string
    if kcount == 1:
        return list(string)
    else:
        newres = []
        for i in range(len(string)): 
            prefix = string[i]
            res = combinationsGenerate(string[i+1:], kcount-1)
            for i in res:
                newres.append(prefix+i)
        return newres    


print combinationsGenerate('arovi', 3)

def fibonacci(n, cache):
    if n in cache:
        return cache[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        cache[n] = fibonacci(n-1, cache) + fibonacci(n-1, cache)
        return cache[n]

assert fibonacci(2,{})==2

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(5)  
root.left = Node(3)
root.right = Node(9)
root.left.right = Node(4)

def inorder(node):
    if node.left:
        inorder(node.left)
    print node.data
    if node.right:
        inorder(node.right)

def preorder(node):
    print node.data
    if node.left: 
        preorder(node.left)
    if node.right:
        preorder(node.right)

def postorder(node):
   if node.left:
       postorder(node.left)
   if node.right:
       postorder(node.right)
   print node.data

print "pre"
preorder(root)
print "inorder"
inorder(root)
print "post"
postorder(root)


def BFS(node):
    import Queue
    q = Queue.Queue()
    q.put(node)
    while not q.empty():
        node = q.get()  
        print node.data
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

print "BFS"
BFS(root)

def DFS(node):
    print node.data
    if node.left:
        DFS(node.left)
    if node.right:
        DFS(node.right)

print "DFS"
DFS(root)


def height_tree(root):
    if root is None:
        return 0
    return 1 + max(height_tree(root.left) , height_tree(root.right))

print "height %s"%height_tree(root)

def check_balanced_tree(root):
    if not root:
        return True, 0 
    lstatus, lheight = check_balanced_tree(root.left) 
    rstatus, rheight = check_balanced_tree(root.right) 
    if not (lstatus and rstatus):
        return False, 1+max(lheight, rheight)
         

# -3 is written as MAX-3 = 5 with sign bit as 1 (negative) 

def tower_of_hanoi(A,B,C,n):
    if n > 0:
        tower_of_hanoi(A,C,B,n-1)  
        if A:
            ele = A.pop()
            C.append(ele)
        tower_of_hanoi(B,A,C,n-1)

A = B = C = []
tower_of_hanoi([1,2,3,4,5],B,C,5)
print C



#  infinite number of 25 cents, 10 cents, 5 nickels, 1 nickel
CENT = [25,10,5,1]
resultset = []
def represent_n_cent(n, cindex):
    if cindex == len(CENT)-1:
        return ["%s:%s"%CENT[index],n]
    else:
        count = 0
        totalcent = 0
        while totalcent <= CENT:
            remain = CENT - totalcent 
            if remain:
                result = represent_n_cent(remain, cindex+1)    
                for i in result:
                    # TODO add for count
            totalcent = CENT[cindex]*count 
                


