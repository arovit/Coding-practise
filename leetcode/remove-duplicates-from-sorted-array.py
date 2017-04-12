#!/usr/bin/python


def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    if len(nums) == 0:
        return 0
    while i < len(nums) -1:
        if nums[i] == nums[i+1]:
            nums.pop(i+1)
        elif nums[i] < nums[i+1]:
            i = i+1
    return i+1
            



