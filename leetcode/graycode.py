#!/usr/bin/python

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        start = [0]
        for i in range(n):
            start += [ele+(2**i)  for ele in reversed(start)]
        return start
