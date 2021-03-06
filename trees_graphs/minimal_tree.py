#!/usr/bin/python

from trees import *

class TreeBuilder:
    """ Minimal Tree builder class """
    visited = []
    def build_tree(self, input_array):
        if len(input_array) == 0:
            return None 
        if len(input_array) == 1:
            return Node(input_array[0])
        else:
            node = Node(input_array[len(input_array)/2])
            node.left = self.build_tree(input_array[:len(input_array)/2])
            node.right = self.build_tree(input_array[(len(input_array)/2) + 1:])
            return node
    def get_root_node(self, array):
        leng = len(array)/2
        node = Node(array[leng])
        return node

trbuild = TreeBuilder()
root = trbuild.build_tree([1,2,3,4,5,6,7,8])
in_order(root)
print root

