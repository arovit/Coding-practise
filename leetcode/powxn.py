#!/usr/bin/python

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1 
        if n%2 == 0: # if n is even
            return self.myPow(x, n/2) * self.myPow(x, n/2)
        else:
            return x * self.myPow(x, n//2) * self.myPow(x, n//2)
       

sol = Solution() 
print sol.myPow(3,3)
