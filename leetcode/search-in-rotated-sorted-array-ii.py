#!/usr/bin/python

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 00111112
        # 20011111
        return self.doBinary(nums, 0, len(nums), target)
    
    def doBinary(self, nums, start, end, target):
        if start > end:
            return False
        middle = (start + end)/2
        if start == middle:
            return nums[middle] == target 
        print start, middle, end
        if nums[middle] > target:
            # target needs to be on left side
            if nums[start] < nums[middle] and target < nums[start]:
                return self.doBinary(nums, middle, end, target)
            elif nums[middle] == nums[start]:  #if start == middle  - look both sides
                return self.doBinary(nums, start, middle, target) or self.doBinary(nums, middle, end, target) 
            else:
                return self.doBinary(nums, start, middle, target)
        elif nums[middle] < target:
            # target needs to be on right side
            if nums[middle] < nums[end-1] and target > nums[end-1]:
                return self.doBinary(nums, start, middle, target)
            elif nums[middle] == nums[end-1]:  #if middle == last  - look both sides
                return self.doBinary(nums, start, middle, target) or self.doBinary(nums, middle, end, target) 
            else:
                return self.doBinary(nums, middle, end, target)
        else: # middle == target
            return True


sol= Solution()
nums = [1,1,1,3,1]
print nums
print sol.search(nums, 2)
