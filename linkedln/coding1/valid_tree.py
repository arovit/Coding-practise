#!/usr/bin/python

# valid tree checker
# input - nodes = [1,2,3,4], edges = [(1,2),(3,4),(2,3)] 

# check 
# Acyclic - number of edges = n-1
# All the nodes are connected ( atleast one path to visit all nodes )

def valid_tree(node, edges):
    """ Check if nodes, edges form valid tree """
    if len(edges) != node-1:
        return False  # edges = node - 1 
    ncon = {i:[] for i in range(node)}
    print ncon
    for e in edges:
        fnode = e[0]
        tnode   = e[1] 
        ncon.get(fnode).append(tnode)
        ncon.get(tnode).append(fnode)
    def visit(node):
        map(visit, ncon.pop(node,[]))  
    visit(0)
    if not ncon:
        return True
    return False

node = 5  # 0, 1
edges = [(1,2),(2,3),(3,4),(2,4)]
print valid_tree(node, edges)
