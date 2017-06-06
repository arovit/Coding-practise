#!/usr/bin/python

import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        permutation = ''
        # logic is (n-1)! starts from lowest and second lowest etc..
        numbers = range(1, n+1)
        k -= 1 
        while n > 0:
            n -= 1
            index, k= divmod(k, math.factorial(n))
            permutation  += "%s"%numbers[index]
            numbers.remove(numbers[index])
        print permutation     
        


sol = Solution()
sol.getPermutation(3, 2)
