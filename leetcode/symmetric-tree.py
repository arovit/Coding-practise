#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkSymmetry(root, root)
        
    def checkSymmetry(self, lnode, rnode):
        if not lnode and not rnode:
            return True
        elif (lnode and rnode) and (lnode.val == rnode.val): # if values are same then compare the symmetrical ndes
            return self.checkSymmetry(lnode.left, rnode.right) and self.checkSymmetry(lnode.right, rnode.left)
        return False
