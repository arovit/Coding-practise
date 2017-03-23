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
     
        schar = [] 
        njump = 1
        while njump < len(data):
            schar.append(data[njump])
            njump = njump + 2*(numRows-3) + 2  
        print ''.join(schar)

        lchar = [] 
        njump = 2
        while (njump > 0) and (njump < len(data)):
            lchar.append(data[njump])
            njump = njump + 2*(numRows-2) + 2
        print ''.join(lchar)

sol = Solution()
sol.convert("arovit", 3) 
