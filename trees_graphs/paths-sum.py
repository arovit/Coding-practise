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

class node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathsSum(node, runningSum, targetSum, hashPaths):
    """ Efficient way to calculate the total paths summing to targetsum """
    totalPaths = 0
    if not node:
       return totalPaths
    runningSum = runningSum + node.data 
    if runningSum == targetSum:
        totalPaths += 1
    sum = runningSum - targetSum
    if sum in hashPaths:
        totalPaths += hashPaths[sum]
    count = hashPaths.get(runningSum,0)
    count +=1 
    hashPaths[runningSum] = count
    totalPaths += pathsSum(node.left, runningSum, targetSum, hashPaths)
    totalPaths += pathsSum(node.right, runningSum, targetSum, hashPaths)
    count = hashPaths.get(runningSum,0)
    count -= 1
    if not count:
        del hashPaths[runningSum]
    else:
        hashPaths[runningSum] = count
    return totalPaths
   
n = node(10)
n.left = node(5)
n.left.left = node(1)
n.left.left.left = node(2)
n.left.left.left.left = node(-1)
n.left.left.left.left.left = node(-1)

print pathsSum(n,0,6,{})

#doBFS(a, 40)






