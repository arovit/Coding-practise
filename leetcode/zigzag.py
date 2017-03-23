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
        mainarr = []
        if numRows == 1:
            return data
        for row in range(numRows):
            njump = row            
            print njump
            temparray = []
            if row > 0 and row < (numRows-1):
                mfactor = 3 
            else:
                mfactor = 2
            while njump < len(data):
                temparray.append(data[njump])
                njump = njump + 2*(numRows-mfactor) + 2
                print "here njump %s"%njump
                if not njump:
                    break 
            print temparray 
            mainarr.append(''.join(temparray))
        return ''.join(mainarr)


sol = Solution()
print sol.convert("ABCDE", 4)
