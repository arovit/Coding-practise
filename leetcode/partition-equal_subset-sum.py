#!/usr/bin/python

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tsum = sum(nums)
        if tsum % 2 != 0:
           return False 
        hsum = tsum/2
        return self.calculate(0, hsum, nums, {})

    def calculate(self, start, targetsum, nums, memoz):
        if targetsum in memoz:
            return memoz[targetsum]
        if targetsum == 0:
            memoz[targetsum] = True
            return True
        else:
            memoz[targetsum] = False 
            if targetsum > 0:
                for i in xrange(start, len(nums)):
                    if self.calculate(i+1, targetsum - nums[i], nums, memoz):
                        memoz[targetsum] = True
                        return True
        return False
         

solver = Solution()
inp = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
print solver.canPartition(inp)
