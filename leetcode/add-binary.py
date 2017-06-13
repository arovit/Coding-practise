#!/usr/bin/python

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            diff = len(a)-len(b)
            b = '0'*diff + b
        elif len(a) < len(b):
            diff = len(b)-len(a)
            a = '0'*diff + a
        result = ''
        i = len(a)-1
        carry = 0
        while i >= 0:
            num = int(a[i]) + int(b[i]) + carry
            if num == 3:
                result = "1" + result
                carry = 1
            elif num == 2:
                result = "0" + result
                carry = 1
            elif num == 1:
                result = "1" + result
                carry = 0
            elif num == 0:
                result = "0" + result
                carry = 0
            i -= 1
        if carry:
            result = "1" + result
        print result
        return result
            

