#!/usr/bin/python

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num = nums
        if len(num) < 2:
            return
        # Find longest sequest from right
        sindex = self.findLongestSeq(num) 
        if (sindex is None) or sindex < 0:
            sindex = -1
        else:
            # Swap two values
            self.swapValues(sindex, num)
        # Reverse the segment of list
        self.reverse(sindex+1, num)

    def reverse(self, index, num):
        i = index
        j = len(num) - 1
        while i < j:
            num[i], num[j] = num[j], num[i]
            i += 1
            j -= 1

    def findLongestSeq(self, num):
        i = len(num)-1
        while i >= 0:
            if num[i] > num[i-1]:
                return i-1 
            else:
                i = i -1
                continue

    def swapValues(self, sindex, num):
        j = sindex+1
        while j < len(num):
            if num[j] <= num[sindex]:
                break
            j += 1
        # swap j-1 and sindex:
        num[j-1], num[sindex] = num[sindex], num[j-1]      

sol = Solution()
inp = raw_input("Enter list ").strip().split(' ')
sol.nextPermutation(inp)
