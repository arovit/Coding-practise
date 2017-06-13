#!/usr/bin/python

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb(n,{})
       
    def climb(self, n, cache):
        if n in cache:
            return cache[n]
        if n < 0:   
            ret = 0
        elif n == 1:
            ret = 1
        elif n == 2:
            ret = 2
        else:
            ret = self.climb(n-1, cache) + self.climb(n-2, cache)
        cache[n] = ret
        return ret
        
