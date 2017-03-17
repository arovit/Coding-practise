#!/usr/bin/python

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        collect_hash = dict()
        strlen = len(s)
        index  = 0
        max_len = 0
        
        while index < strlen: 
            if not s[index] in collect_hash:
                collect_hash[s[index]] = index
                index += 1
            else:
                max_len = max(max_len, len(collect_hash))
                index = collect_hash[s[index]] + 1
                collect_hash = dict()
        max_len = max(max_len, len(collect_hash))
        return max_len

