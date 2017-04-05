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
            if index != len(timeSeries): 
                if (timeSeries[index+1] - timeSeries[index]) < duration:
                    mduration = mduration + (timeSeries[index+1] - timeSeries[index])
                else:
                    mduration = mduration + duration       
        print mduration

Solution()
