#!/usr/bin/python 


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
     def __str__(self):
        print "Data %s, left - %s, right - %s"%(self.val, self.left, self.right)

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nodes = range(1,n+1)
        import copy
        return self.formTrees(nodes)
         
    def formTrees(self, nodes):
        if not nodes:
            return []
        if len(nodes) == 1:
            return [TreeNode(nodes[0])]
        resultantList = []
        for i in range(len(nodes)):
            mnode = TreeNode(nodes[i])
            ltrees = self.formTrees(nodes[:i])
            rtrees = self.formTrees(nodes[i+1:])
            if not ltrees:
                for r in rtrees:
                    mnode = copy.deepcopy(mnode)
                    mnode.right = r
                    resultantList.append(mnode)
            if not rtrees:
                for l in ltrees:
                    mnode = copy.deepcopy(mnode)
                    mnode.left = l
                    resultantList.append(mnode)
            for l in ltrees:
                for r in rtrees:
                    mnode = copy.deepcopy(mnode)
                    mnode.left = l
                    mnode.right = r
                    resultantList.append(mnode)
        return resultantList             
        

sol = Solution()
sol.generateTrees(3)
