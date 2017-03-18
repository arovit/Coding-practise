#!/usr/bin/python

class Solution(object):
    def reverse(self, x):
        import math
        last_char = []
        positive = True
        if x < 0:
            positive = False 
            x = x * -1  ## make it positive 
        while x:
           num = x % 10
           last_char.append(num) 
           x = x / 10 
        num = 0
        for index, val in enumerate(last_char[::-1]):
            num = int(num + val * math.pow(10, index))
        if not positive:
            num = num * -1
        if positive and num > 2147483647:
            return 0
        elif (not positive) and num < -2147483648: 
            return 0
        else:
            return num 
sol = Solution()
print sol.reverse(123)
