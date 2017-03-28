#!/usr/bin/python

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ilen = self.getLength(x)
        half = ilen/2
        if ilen % 2 == 0:
            skipm = False
        else:
            skipm = True
        nstack = []
        for i in range(0,half):
            rem = x%10
            nstack.append(rem)
            x = x/10
        if skipm:
            x = x/10
        #print x, nstack
        for i in range(0,half):
            rem = x %10
            ele = nstack.pop()
            #print rem, ele
            if ele != rem:
               return False
            x = x/10
        return True

    def getLength(self, x):
        count = 0
        while x:
            x = x/10
            count += 1
        return count
    
