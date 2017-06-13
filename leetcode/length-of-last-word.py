#!/usr/bin/python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastLen = 0
        s = s.strip()
        totLen = len(s)
        for i in range(totLen-1, -1, -1):
            if s[i] == ' ':
                break
            lastLen += 1
        return lastLen

