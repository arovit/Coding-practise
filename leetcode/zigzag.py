#!/usr/bin/python

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        data = s
        fchar = []
        njump = 0
        while njump < len(data):
            fchar.append(data[njump])
            njump = njump + 2*(numRows-2) + 2   
        print ''.join(fchar) 


sol = Solution()
sol.convert("arovit", 3) 
