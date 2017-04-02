#!/usr/bin/python

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_num = 0
        for index, val in enumerate(strs):
            if strs[index][common_num] != strs[index+1][common_num]:
                break
            else
                common_num += 1 
