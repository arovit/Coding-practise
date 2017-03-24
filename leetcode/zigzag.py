#!/usr/bin/python

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        data = s
        if numRows == 1:
            return data
        import math
        strlen = len(data)
        blocklen = (numRows - 2)*2 + 2
        finalStr = []
        numblocks = int(math.ceil(float(strlen)/blocklen))
        for rownum in range(numRows):
            findex1 = findex2 = ''
            for bindex in range(numblocks):     
                if (rownum == 0):
                    findex1 = bindex * blocklen
                    #print findex1, data[findex1]
                elif (rownum == (numRows - 1)):  
                    findex1 = (rownum) + (bindex)* blocklen
                    #print findex1
                else:
                    findex1 = (bindex * blocklen) + (rownum)
                    findex2 = findex1 + ((numRows-1)-(rownum+1)) * 2 +2 
                if findex1 != '' and findex1 < len(data):
                    finalStr.append(data[findex1])
                if findex2 != '' and findex2 < len(data):
                    finalStr.append(data[findex2])
                findex1 = findex2 = '' 
        return ''.join(finalStr)
sol = Solution()
print sol.convert("abcderfg", 2)
