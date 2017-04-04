#!/usr/bin/python

import graph
import Queue

def BFS(root):
    """ Perform the BFS search operation """
    q = Queue.Queue()    
    q.put(root)
    visited = []
    while q.qsize() > 0:
        node = q.get()
        if node in visited:  ## if the node is already visited
            continue
        print node.data
        for i in node.children:
            q.put(i)
        visited.append(node)


def DFS(root, visited):
    """ Perform the DFS search """ 
    if not root:
        return
    for i in root.children:
        if not i in visited:
            visited.append(i)
            DFS(i, visited)
    print root.data 

print "BFS:"
BFS(graph.node)

print "DFS:"
DFS(graph.node, [])
