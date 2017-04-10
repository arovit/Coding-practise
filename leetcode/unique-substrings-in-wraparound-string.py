#!/usr/bin/python



class Solution(object):
    
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        self.resultSubString = {}
        lc = 0
        total = 0
        pc = None
        for index, val in enumerate(p):
            if pc and ((ord(pc) == ord(p[index])-1) or (ord(pc) == 122 and ord(p[index]) == 97)):
                lc += 1 
            else:
                lc = 1
            self.resultSubString[p[index]] = max(self.resultSubString.get(p[index], 1), lc)
            pc = p[index]
        for _, val in self.resultSubString.items():
            total += val 

        return total 

solver = Solution()
estr = raw_input("Enter string").strip()
print solver.findSubstringInWraproundString(estr)
