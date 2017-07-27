class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Classic Dynamic programming
        rows = cols = len(s)
        palinds = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(len(s)):
            palinds[i][i] = 1   # all single chars are palindromes
            if i != len(s)-1:
                if s[i] == s[i+1]:
                    palinds[i][i+1] = 1  
        for plen in range(2, len(s)):
            for i in range(len(s)-plen):
                j = i + plen
                if s[i] == s[j] and palinds[i+1][j-1]:
                    palinds[i][j] = 1
        count = 0
        for i in range(len(palinds)):
            count += sum(palinds[i])
        return count
