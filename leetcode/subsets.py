#!/usr/bin/python

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resultant = []
        for i in range(1,len(nums)+1):
            resultant.extend(self.generate_all_subsets(nums, i))
        resultant.append([])
        return resultant
    
    def generate_all_subsets(self, nums, k):
        if k == len(nums):
            return [nums]
        elif k == 1:
            return [[i] for i in nums]
        else:
            tmp1 = self.generate_all_subsets(nums[1:], k)
            tmp2 = self.generate_all_subsets(nums[1:], k-1)
            for i in tmp2:
                i.append(nums[0])
            return tmp1 + tmp2
