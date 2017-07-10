#!/usr/bin/python

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        height = self.getHeight(root)
        print height
        self.level_order = [[] for i in range(height)]
        self.levelPrint(root,0)
        return self.level_order

    def levelPrint(self, node, level):
        if not node:
            return
        self.level_order[level].append(node.val)
        self.levelPrint(node.left, level+1)
        self.levelPrint(node.right, level+1)
        
    def getHeight(self, node):
        if not node:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
