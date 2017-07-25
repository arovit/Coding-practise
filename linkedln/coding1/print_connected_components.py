#!/usr/bin/python



##Connected Components in an undirected graph 
## again emphasis on neighbour dict and visit logic


def connected_components(nodes, edges):
    visited = {i:0 for i in nodes}
    ncon = {i:[] for i in nodes}
    for i in edges:
        ncon[i[0]].append(i[1])
        ncon[i[1]].append(i[0])

    def visit(node, nlist):
        if visited[node]:
            return
        visited[node] = 1
        nlist.append(node) 
        map(lambda x: visit(x, nlist), ncon.pop(node,[])) 

    for i in nodes:
        if not visited[i]:
            alln = []
            visit(i,alln)
            print alln
    

nodes = [0,1,2,3,4,5]
edges = [(0,1),(1,2),(3,4),(4,5)]
connected_components(nodes, edges)   
