#!/usr/bin/python

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter
        dictnum = Counter(nums)
        dnums = dictnum.keys()
        return self.generateSets(dnums, dictnum)
    
    def generateSets(self, nums, rdict):
        if len(nums) == 1:
            result = [[]]
            times = rdict[nums[0]]
            for i in range(1,times+1):
                result.append([nums[0]]*i)
            return result
        # group the same elements
        newresult = []
        rset = self.generateSets(nums[1:], rdict)
        newresult.extend(rset)
        for s in rset:
            times = rdict[nums[0]]
            for i in range(1,times+1):
                newresult.append([nums[0]]*i+s)
        return newresult
