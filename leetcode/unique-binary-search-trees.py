#!/usr/bin/python

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.hashvals = {}
        return self.generateTrees(n) or 1
        
    def generateTrees(self, value):
        if value in self.hashvals:
            return self.hashvals[value]
        if value <= 2:
            return value
        totalTrees = 0
        for i in range(value):
            lnodes = i        # left nodes
            rnodes = value-i-1  # right nodes
            lval = self.generateTrees(lnodes) or 1  # can never be zero
            rval = self.generateTrees(rnodes) or 1  # can never be zero
            totalTrees += (lval * rval)
        self.hashvals[value] = totalTrees
        return totalTrees
    
            
        
