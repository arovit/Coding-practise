#!/usr/bin/python

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.keyhash = {}
        self.memoize = {} 
        self.mlist = []
        for i in range(len(nums)):
            self.doRecursive(i, len(nums)-1, nums, 0, target, [])
        print self.mlist
 
    def doRecursive(self,start,end, nums, length, target, resultset):
        if length > 4:
            return False
        if length == 4 and target == 0:
            keyhash = "#".join(map(str,resultset[:]))
            if not keyhash in self.keyhash: 
                self.mlist.append(resultset[:]) 
                self.keyhash[keyhash] = 1 
            return True
        for i in range(start, end+1):
            resultset.append(nums[i])
            self.doRecursive(i+1, end, nums, length +1, target-nums[i], resultset):
            resultset.pop()

l = raw_input("Enter the list").strip().split(' ')
l = map(int, l)
t = raw_input("Enter the target").strip()
t = int(t)
sol = Solution()
sol.fourSum(l, t)
