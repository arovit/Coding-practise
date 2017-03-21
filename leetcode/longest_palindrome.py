#!/usr/bin/python

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.data = s
        h = w = len(s)
        self.palinar = [ [0 for i in range(w)] for j in range(h) ]
        self.maxlen = 0
        self.palin = []
        for i in range(0, len(self.data)):    ## single char is a palindrome
            self.palinar[i][i] = 1
            self.maxlen = 1
            self.palin = self.data[i]

        for i in range(0, len(self.data)-1):  ## check two consecutive chars
            if self.data[i] == self.data[i+1]:
               self.palinar[i][i+1] = 1
               self.maxlen = 2
               self.palin = self.data[i:i+2]
        #print self.data 
        for i in range(3, len(self.data)+1):   ## Distance array
            for j in range(0, len(self.data)-i+1):  ## Starting index
                k = j + i - 1 
                #print "%s %s - %s"%(j, k , i)
                if self.palinar[j+1][k-1] and (self.data[j] == self.data[k]):
                    #print "palin %s %s"%(j,k) 
                    self.palinar[j][k] = 1 
                    if i > self.maxlen:
                        self.maxlen = i
                        self.palin = self.data[j:k+1]
          
        return self.palin            
       

sol = Solution()
print sol.longestPalindrome("cbbd")
