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
        if not nums:
            rlist = [-1, -1] 
        elif len(nums) == 1:
            if nums[0] == target:
                rlist = [0,0]
            else:
                rlist = [-1, -1] 
        else: 
            min_index = self.binarySearchFirst(nums, target, 0, len(nums)-1, 1, None)
            max_index = self.binarySearchFirst(nums, target, 0, len(nums)-1, None, 1)
            if  min_index is None:
                rlist = [-1, -1]
            else:
                rlist = [min_index, max_index]
        return rlist

    def binarySearchFirst(self, nums, target, start, end, left=None,right=None):
        middle = (start + end)/2 
        print start, middle, end
        if start == end:
            if nums[start] == target:
                return start
            else:
                return None 
        elif start > end:
            return None
        middle = (start + end)/2 
        time.sleep(1)
        if nums[middle] < target: ## search right side
            if middle != len(nums)-1: 
                val = self.binarySearchFirst(nums, target, middle+1, end, left, right) 
            else:
                return None
        elif nums[middle] > target:  ## search left side
            if middle != 0: 
                val = self.binarySearchFirst(nums, target, start, middle-1, left, right) 
            else:
                return None
        else:  # both are same - search left side
            if left:
                if middle != 0: 
                    val = self.binarySearchFirst(nums, target, start, middle-1, left, right)
                    if val is None:
                        return middle 
                    else:
                        return val
                else:
                    return middle
            if right:
                if  middle != len(nums)-1:
                    val = self.binarySearchFirst(nums, target, middle+1, end, left, right)
                    print val
                    if val is None:
                        return middle 
                    else:
                        return val
                else:
                    return middle
        return val 

sol = Solution()
nums = map(int, raw_input('Enter list ').strip().split(' '))
target = input('Enter target ')
print sol.searchRange(nums, target) 
