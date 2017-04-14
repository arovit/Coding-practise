#!/usr/bin/python

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.mlist = []
        for i in range(len(nums)):
            self.doRecursive(i, len(nums)-1, nums, 0, target, [])
        print self.mlist
 
    def doRecursive(self,start,end, nums, length, target, resultset):
        if length > 4:
            return
        for i in range(start, end+1):
            newtarget = target - nums[i]
            if length == 4 and newtarget == 0:
                resultset.append(nums[i])
                self.mlist.append(resultset) 
                resultset.pop()
                return True
            else:
                resultset.append(nums[i])
                self.doRecursive(i+1, end, nums, length +1, newtarget, resultset)
                resultset.pop()

l = raw_input("Enter the list").strip().split(' ')
l = map(int, l)
t = raw_input("Enter the target").strip()
t = int(t)
sol = Solution()
sol.fourSum(l, t)
