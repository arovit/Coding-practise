#!/usr/bin/python

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        NHash = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        Integral = []
        data = str
        data = data.strip()
        if not data:
            return 0
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        sign_found = False
        mul = 1
        for i in data:
            if i in NHash:
                Integral.append(NHash[i]) 
            else: 
                if i in ['-','+'] and (not sign_found):
                    if len(Integral) > 0:
                        break
                    else:
                        if i == '-':
                            mul = -1
                        elif i == '+':
                            mul = 1 
                        sign_found = True
                else:
                    if not Integral:
                        Integral = [0]
                    break 
        print Integral
        n = len(Integral)
        sum = 0
        import math
        for i in range(n):
            sum = sum + int(math.pow(10, (n-1)-i))*Integral[i]
        sum = sum * mul
        if sum > MAX_INT:
            sum = MAX_INT
        elif sum < MIN_INT:
            sum = MIN_INT
        else:
            pass
        print sum


mystr = raw_input()
sol = Solution()
sol.myAtoi(mystr)
