#!/usr/bin/python

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)   # length of the string
        if s[::-1] == s:
            return len(s)
        lpalin = [ [0 for i in range(n)] for j in range(n)]
        for i in range(n):
            lpalin[i][i] = 1  # single char is a palindrome
        
        for plen in range(2, n+1):      # palindrom len start from 2, max - n
            for i in range(0,n-plen+1):  # startchar = 0-last char depending upon len
                j = i+plen-1             # endchar = start + palin length-1
                if s[i] == s[j] and (plen == 2):         # two strings
                    lpalin[i][j] = 2
                elif s[i] == s[j]:       # inner palin + 2 corner
                    lpalin[i][j] = lpalin[i+1][j-1] + 2
                else:                   # both are different
                    lpalin[i][j] = max(lpalin[i][j-1], lpalin[i+1][j])
        return lpalin[0][n-1]
                    
