class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = nums[0]
        i = 0
        while i <= max_index and i < len(nums):
            max_index = max(nums[i]+i, max_index)
            i += 1
        if max_index >= len(nums)-1:
            return True
        return False
            
