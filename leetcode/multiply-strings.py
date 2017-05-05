#!/usr/bin/python

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        self.addlist = []
        if len(num2) < len(num1):
            num1, num2 = num2, num1 
        for index, i in enumerate(num1[-1::-1]):
            rlist = []
            overflow = 0
            for k in range(1, index+1):
                rlist.append(0)  
            for j in num2[-1::-1]:
                result = ( int(i) * int(j) ) + overflow
                remain = result % 10
                overflow = result/10
                rlist.append(str(remain))
            if overflow:  
                rlist.append(str(overflow))
            self.addlist.append(rlist)

        print self.listsum
        summedlist = self.listsum(self.addlist) 
        mnumber = "".join(map(str,summedlist[::-1]))
        return mnumber
     
    def listsum(self, listOfList):
        max_range = 0 
        for i in listOfList:
            if len(i) > max_range:
                max_range = len(i)
        overflow = 0 
        sumresult = []
        for i in range(max_range):
            totalsum = overflow
            for templ in listOfList:
                if i < len(templ):
                    totalsum += int(templ[i])
            remain = totalsum % 10
            overflow = totalsum/10
            sumresult.append(remain)
        if overflow:
            sumresult.append(overflow)     
        return sumresult 

sol = Solution()
inp1 = raw_input("inp 1").strip()
inp2 = raw_input("inp 2").strip()
print sol.multiply(inp1, inp2)
