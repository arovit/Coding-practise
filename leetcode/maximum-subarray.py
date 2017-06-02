#!/usr/bin/python


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_matrix = [0 for i in range(len(nums)+1)]
        dp_matrix[0] = nums[0]
        max_sum = nums[0]
        
        for i in range(1,len(nums)):
            if dp_matrix[i-1] > 0:
                temp = dp_matrix[i-1]
            else:
                temp = 0  
            dp_matrix[i] = nums[i] + temp
            max_sum = max(max_sum, dp_matrix[i])
        return max_sum
