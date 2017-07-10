#!/usr/bin/python

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # logic whenever you go dip, keeping looking back
        heights.append(0)   # just in case it keeps increasing
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:  # when heights[i] is less than top of stack means we are dipping
                while heights[i] < heights[stack[-1]]:  # run a while loop till we find height < stack[-1]
                    index =  stack.pop()    # last height
                    h = heights[index]
                    w = i - stack[-1] - 1   # distance of i to top of stack -1
                    if h * w > max_area:    
                        max_area = h * w   
                stack.append(i)
        heights.pop()
        return max_area
