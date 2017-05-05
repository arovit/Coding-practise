#!/usr/bin/python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.upermutation = []
        self.permutation_generate([], nums)
        print self.upermutation
        

    def permutation_generate(self, prefix, inp_strn):
        if not inp_strn:
            self.upermutation.append(prefix[:])
        else:
            local_hash = {}
            for i in range(len(inp_strn)):
                if not inp_strn[i] in local_hash:
                    local_hash[inp_strn[i]] = 1 
                    prefix.append(inp_strn[i])
                    self.permutation_generate(prefix, inp_strn[:i]+inp_strn[i+1:])
                    prefix.pop()


sobj = Solution()
sobj.permuteUnique([1,2,1])
