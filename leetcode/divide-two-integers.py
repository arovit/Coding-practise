#!/usr/bin/python

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        counter = 0 
        minus = 0
        if (dividend < 0) and (divisor < 0):
            minus = 0
        elif dividend < 0:
            minus = 1   
        elif divisor < 0:
            minus = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            counter = dividend
        else:
            while dividend >= divisor:
                div, i  =   divisor, 1 
                while dividend >= div:  
                    dividend = dividend - div
                    counter += i
                    i = i << 1
                    div = div << 1
        if minus:
            counter = counter * -1 
        if counter < -2147483648:
            return -2147483648
        if counter > 2147483647:
            return 2147483647

        return counter


sol = Solution()
print sol.divide(10,-2)
