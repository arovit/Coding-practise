class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            replace = False
            for j in range(i-1, -1, -1):
                if nums[j] <= nums[i]:
                    if replace:
                       temp = nums[i]
                       nums.insert(j+1, temp)
                       nums.pop(i+1)
                       replace = False
                    break
                if nums[j] > nums[i]:
                    replace = True
                    continue
            if replace:
                j = -1
                temp = nums[i]
                nums.insert(j+1, temp)
                nums.pop(i+1)
                replace = False
