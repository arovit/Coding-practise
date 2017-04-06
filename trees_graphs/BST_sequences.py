#!/usr/bin/python


import trees


def allSequences(node):
    result = [] 
    if not node:
        result.append([])  
        return result
    prefix = []
    prefix.append(node.data)
    leftSeq = allSequences(node.left)
    rightSeq = allSequences(node.right)
    
    for left in leftSeq:
        for right in rightSeq:
            weaved = []
            weaveLists(left, right, weaved, prefix)
            result.extend(weaved)
    return result


def weaveLists(first, second, results, prefix):
    """ Merge two lists to keep them in same order"""
    if len(first) == 0 or len(second) == 0:
        result = prefix[:] 
        result.extend(first)
        result.extend(second)
        results.extend(result)
        return
    
    headFirst = first.pop(0)
    prefix.append(headFirst)
    weaveLists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, headFirst)
    
    headSecond = second.pop(0)
    prefix.append(headSecond)
    weaveLists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, headSecond)
     

a = trees.Node(50)
b = a.addleft(48)
i = a.addright(52)
c = b.addleft(25)
print a
print allSequences(a)
