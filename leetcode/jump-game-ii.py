#!/usr/bin/python
import sys
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distance = [sys.maxint for i in range(len(nums))]
        distance[0] = 0
        last_step = 0
        for i in range(len(nums)):
            if i+nums[i] > last_step :
                last_step = i+nums[i]
            else:
                continue    
            step = 1 
            while (step <= nums[i]) and (step+i < len(nums)):
                if distance[i+step] > distance[i] + 1:
                    distance[i+step] = distance[i] + 1
                step = step + 1
        return distance[len(nums)-1]


sol = Solution()
print sol.jump([2,3,1,1,4])
                    
        
