#!/usr/bin/python

from trees import Node

n = Node(10)
l1 = n.addleft(2)
r1 = n.addright(20)
l2 = l1.addleft(13)
l3 = l2.addleft(13)
lr2 = l3.addright(19)


def get_height(node):
     if not node:
         return 0
     lh = get_height(node.left)
     rh = get_height(node.right) 
     return max(lh, rh) + 1
   
level_list = {} 

def create_level_list(node, level):
    if not node:
        return
    temp = level_list.get(level, [])
    temp.append(node.data) 
    level_list[level] = temp
    create_level_list(node.left, level+1) 
    create_level_list(node.right, level+1) 
    return
    
create_level_list(n, 0)

print level_list
     
