#!/usr/bin/python

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashes = {}
        if not nums:
            return 1
        for i in nums:
            hashes[i] = 1
        nmin = min(nums)
        nmax = max(nums)
        for i in xrange(1, nmax):
            if i not in hashes:
                nfound = i
                break
        else:
            nfound = nmax+1
        return nfound
