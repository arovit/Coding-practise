#!/usr/bin/python


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water_area = 0
        max_value_index = height.index(max(height))
        for i in range(max_value_index)):
            if height[i] > height[i+1]:
                water_area = water_area + (height[i] - height[i+1])
                height[i+1] = height[i] 
        for i in range(len(height)-1, max_value_index, -1):
            if height[i] > height[i-1]:
                water_area = water_area + (height[i] - height[i-1])
                height[i-1] = height[i] 
        return water_area
