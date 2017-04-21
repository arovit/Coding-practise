#!/usr/bin/python

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.doBinarySearch(nums, target, 0, len(nums)-1)

    def doBinarySearch(self, nums, target, start, end):
        middle = (start + end)/2 
        print start, middle, end
        if start > end: 
            return -1 
        elif start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        if nums[middle] == target:
            return middle
        elif nums[middle] >= nums[start]:                      ## Left is sorted
            if nums[middle] > target >= nums[start]:
                return self.doBinarySearch(nums, target, start, middle-1)
            else:                                             ## target not in left - search in right 
                return self.doBinarySearch(nums, target, middle+1, end)  #target in right
        elif nums[middle] <= nums[end]:                        ## right is sorted
            if nums[middle] < target <= nums[end]:            ## target in right
                return self.doBinarySearch(nums, target, middle+1, end) 
            else:                                             ## target in left
                return self.doBinarySearch(nums, target, start, middle-1) 



sol = Solution()
nums = map(int, raw_input("Enter the list ").strip().split(' '))
target = input("Enter target ")
print sol.search(nums, target)
