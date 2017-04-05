#!/usr/bin/python

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int] [1, 4], 2
        :type duration: int         
        :rtype: int                  
        """
        mduration = 0
        for index, val in enumerate(timeSeries):
            if index != len(timeSeries)-1: 
                if (timeSeries[index+1] - timeSeries[index]) < duration:
                    mduration = mduration + (timeSeries[index+1] - timeSeries[index])
                else:
                    mduration = mduration + duration
            elif index == (len(timeSeries) -1):
                mduration = mduration + duration
    
        return mduration

sol = Solution()
inp = raw_input("Enter the timeSeries")
ts = [int(x) for x in inp.strip().split(' ')]
inp = raw_input("Enter the Duration")
dur = int(inp.strip())
print sol.findPoisonedDuration(ts, dur) 

