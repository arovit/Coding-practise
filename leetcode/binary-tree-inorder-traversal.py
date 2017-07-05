#!/usr/bin/python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder_list = []
        current = root
        stack_nodes = []
        while True:
            if current:
                stack_nodes.append(current)         ## push the node in stack
                current = current.left
            else:
                if stack_nodes:
                    lnode = stack_nodes.pop()           ## get the last left node
                    inorder_list.append(lnode.val)
                    current = lnode.right
                else:
                    break
        print inorder_list              
        return inorder_list
