#!/usr/bin/python
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        tsum = 0
        minL = 0
        while right < len(nums):
            tsum = tsum + nums[right]
            while tsum >= s and left <= right:
              leng = right - left + 1
              if minL == 0:
                  minL = leng
              elif leng < minL:
                  minL = leng
              tsum = tsum - nums[left]
              left = left + 1
            right = right + 1
        return minL
