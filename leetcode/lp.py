#!/usr/bin/python

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 2:
            if not s:
                return ""
            elif len(s) == 1:
                return s[0]
            else:
                if s[0] == s[1]:
                    return s
                else:
                    return ""
            
        pmatrix = [[0 for i in range(len(s))] for i in range(len(s))]
        max_len = 0
        palin = ""
        for i in range(len(s)):
            pmatrix[i][i] = 1  # single char is a  palindrome
            max_len = 1
            palin = s[i]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                max_len = 2 
                palin = s[i:i+2]
                pmatrix[i][i+1] = 1
        for i in range(len(s)):
            for j in range(i+2,len(s)):
                if s[i] == s[j] and (pmatrix[i+1][j-1] == 1):
                    pmatrix[i][j] = 1
                    if (j-i+1) > max_len:
                        max_len = j-i+1
                        palin = s[i:j+1]
        print pmatrix
        return palin 

inp = "abcba"
sol = Solution()
print sol.longestPalindrome(inp)
