#!/usr/bin/python

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        findex = None
        for index, val in enumerate(nums):
            if val >= target:
                findex = index
                break
        if findex is None: findex = len(nums)
        return findex
