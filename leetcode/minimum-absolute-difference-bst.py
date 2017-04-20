#!/usr/bin/python


class Solution(object):
    def getMinimumDifference(self, root, min=999999999999):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            lr = self.rightmost(root.left)
            if abs(lr.val - root.val) < min:
                min = abs(lr.val - root.val)
        if root.right:
            lc = self.leftmost(root.right)
            if abs(lc.val - root.val) < min:
                min = abs(lc.val - root.val)
        if root.left:
            lr = self.getMinimumDifference(root.left, min)
            if lr < min:
               min = lr
        if root.right:
            lc = self.getMinimumDifference(root.right, min)
            if lc < min:
               min = lc
        return min

    def rightmost(self, node):
        if node.right:
            return self.rightmost(node.right)
        else:
            return node

    def leftmost(self, node):
        if node.left:
            return self.leftmost(node.left)
        else:
            return node
