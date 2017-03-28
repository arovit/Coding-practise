#!/usr/bin/python

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        max_i = 0
        while i < j:
            max_i = max(min(height[i], height[j]) * (j-i), max_i)
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1 
        return max_i 
        
sol = Solution()
print sol.maxArea([1,1])
