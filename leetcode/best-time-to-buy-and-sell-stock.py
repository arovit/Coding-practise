#!/usr/bin/python

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxamt = 0
        for index, val in enumerate(prices):
            if index != len(prices)-1:
                if prices[index+1] - prices[index] > 0:
                    maxamt = maxamt + (prices[index+1] - prices[index])
            
        return maxamt    
