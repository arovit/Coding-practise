#!/usr/bin/python

import sys
from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = defaultdict(int)
        for c in t:
            map[c] += 1 
        counter = len(t)
        begin = 0
        end = 0
        head = 0
        d = sys.maxint 
        while end < len(s):
            if map[s[end]] > 0: # s is in t
                counter -= 1    # reduce count
            map[s[end]] -= 1
            end += 1
            while counter == 0:
                if end-begin < d:
                    head = begin
                    d = end-head    
                if map[s[begin]] == 0:
                    counter += 1     
                map[s[begin]] += 1
                begin += 1

        return ("" if d == sys.maxint else s[head:head+d+1])


sol = Solution()
print sol.minWindow("ADOBECODEBANC", "ABC")
