#!/usr/bin/python

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        ncounts = Counter(nums)
        incr_index = 0
        i = 0
        while i < len(nums):
            ntimes = ncounts[nums[i]]
            if ntimes >= 2:
                nums[incr_index] = nums[i]
                nums[incr_index+1] = nums[incr_index]
                i += ntimes
                incr_index += 2
            else:
                nums[incr_index] = nums[i]
                i += 1
                incr_index += 1
        return incr_index
             
