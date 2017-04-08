#!/usr/bin/python



class Solution(object):
    
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        self.resultSubString = []
        lasts = 0
        for index, val in enumerate(p):
            if index == len(p) -1 :
                ele = p[lasts:index+1]
                if not ele in self.resultSubString: 
                    self.resultSubString.append(ele)
                break
            lefto =  ord(p[index]) + 1
            righto =  ord(p[index+1]) 
            if lefto == 123: lefto = 97
            if lefto != righto:
                ele = p[lasts:index+1]
                if not ele in self.resultSubString:
                    self.resultSubString.append(ele)
                lasts = index + 1
        newlist = self.checkArray(self.resultSubString)
        print newlist
        sum = 0
        #for j in self.resultSubString:
        #    sum = sum + self.factorial(len(j))
        #print sum 

    def checkArray(self, array):
        newlist = []
        for i in range(len(array)-1):
            for j in range(len(array)):
                if ((array[i] in array[j]) or (array[j] in array[i])):
                    newlist.append(array[i])
                    break  
            else:
               newlist.append(array[i]) 
        return newlist

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)   

solver = Solution()
estr = raw_input("Enter string").strip()
solver.findSubstringInWraproundString(estr)
