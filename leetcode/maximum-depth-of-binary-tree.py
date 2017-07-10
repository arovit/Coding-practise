#!/usr/bin/python


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = self.getHeight(root)
        return depth
        
    def getHeight(self, node):
        if not node:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
