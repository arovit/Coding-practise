#!/usr/bin/python


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif (p or q) and not (p and q):  # if one of them is empty
            return False
        else:
            if p.val == q.val and \
                        self.isSameTree(p.left, q.left) and \
                        self.isSameTree(p.right, q.right):
                return True
            else:
                return False
 
        
