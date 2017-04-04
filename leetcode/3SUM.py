#!/usr/bin/python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        hashed_entry = {}
        for i in xrange(len(nums)):
            start = i + 1 
            end = len(nums)-1
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    entry="%s#%s#%s"%(nums[i], nums[start], nums[end])
                    if not entry in hashed_entry:
                        result.append([nums[i], nums[start], nums[end]])
                        hashed_entry[entry] = 1
                    end = end - 1   
                elif nums[i] + nums[start] + nums[end] > 0:
                    end = end - 1
                else:
                    start = start + 1
        return result

solver = Solution()
input_list =  [0,0]*10000
print solver.threeSum(input_list)
