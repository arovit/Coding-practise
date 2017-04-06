#!/usr/bin/python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys
        mdist = sys.maxint
        msum = 0
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tsum = nums[i] + nums[j] + nums[k]
                if tsum == target:
                    return tsum
                dist = abs(tsum - target)
                if dist < mdist:
                    mdist = dist
                    msum = tsum
                if tsum > target:
                    k = k - 1
                elif tsum < target:
                    j = j + 1
        return msum


solver = Solution()
inp = raw_input('Enter the list')
nums = [int(x) for x in inp.split(' ')]
inp = raw_input('Enter the target')
tar = int(inp)
solver.threeSumClosest(nums, tar)
