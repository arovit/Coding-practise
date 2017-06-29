#!/usr/bin/python

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # using newton's approximation
        guess = x
        while guess*guess > x:
            guess = (x/guess+guess)/2
        return guess
