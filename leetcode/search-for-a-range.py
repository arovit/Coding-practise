#!/usr/bin/python

import time
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rlist = []
        if len(nums) == 1:
            if nums[0] == target:
                rlist = [0,0]
        else: 
            min_index = self.binarySearchFirst(nums, target, 0, len(nums)-1, 1, None)
            max_index = self.binarySearchFirst(nums, target, 0, len(nums)-1, None, 1)
            if  not min_index:
                rlist = [-1, -1]
            else:
                rlist = [min_index, max_index]
        return rlist

    def binarySearchFirst(self, nums, target, start, end, left=None,right=None):
        middle = (start + end)/2 
        if ((end - start) <= 1):
            return None
        print start, middle, end
        if nums[middle] < target: ## search right side
            val = self.binarySearchFirst(nums, target, middle, end, left, right) 
        elif nums[middle] > target:  ## search left side
            val = self.binarySearchFirst(nums, target, start, middle, left, right) 
        else:  # both are same - search left side
            if left:
                val = self.binarySearchFirst(nums, target, start, middle, left, right)
                print val
                if val is None:
                    return middle 
                else:
                    return val
            if right:
                val = self.binarySearchFirst(nums, target, middle, end, left, right)
                if val is None:
                    return middle 
                else:
                    return val
        return None

sol = Solution()
nums = map(int, raw_input('Enter list ').strip().split(' '))
target = input('Enter target ')
print sol.searchRange(nums, target) 
