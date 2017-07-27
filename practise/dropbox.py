#!/usr/bin/python



# binary search

def binary(startindex, endindex, elements, target):
    if startindex > endindex:
        return False
    middleindex = (endindex + startindex)/2
    if elements[middle] > target:
        return binary(middleindex, endindex, elements, target)
    elif elements[middle] < target:
        return binary(startindex, middleindex, elements, target)
    else:
        return middleindex


def inorder_traversal(node):
    if node.left:
        inoder_traversal(node.left)
    print node.data
    if node.right:
        inoder_traversal(node.right)


