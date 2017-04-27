#!/usr/bin/python

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        print self.getsequence(n) 

    def getsequence(self, n):
        if n == 1:
            return "1"
        else:
            laststr = self.getsequence(n-1)
            return self.say(laststr)
            
    def say(self, strn):
        reply = ""
        for index, val in enumerate(strn):
            if index==0:
                prev = val
                count = 1
            else:
                if (val == prev):
                    count += 1
                elif val != prev :
                    reply = reply + "%s%s"%(count, prev)
                    prev = val
                    count = 1
            if index == (len(strn) -1):
                reply = reply + "%s%s"%(count, prev)
        return reply 


sol = Solution()
sol.countAndSay(3)
