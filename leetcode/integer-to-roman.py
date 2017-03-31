#!/usr/bin/python


class Solution:
    def intToRoman(self, num):
        symbols = {'I':1, 'V':5 , 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }           
        result = "" 
        while num > 0:       
            print num
            if num >= 1000:
                result += "M"  
                num = num - 1000 
            elif num >= 900:
                result += "CM"
                num = num - 900 
            elif num >= 500:
                result += "D"
                num = num - 500 
            elif num >= 400:
                result += "CD"
                num = num - 400 
            elif num >= 100:
                result += "C"
                num = num - 100 
            elif num >= 90:
                result += "XC"
                num = num - 90 
            elif num >= 50:
                result += "L"
                num = num - 50 
            elif num >= 40:
                result += "XL"
                num = num - 40 
            elif num >= 10:
                result += "X"
                num = num - 10
            elif num >= 9:
                result += "IX"
                num = num - 9 
            elif num >= 5:
                result += "V"
                num = num - 5
            elif num >= 4:
                result += "IV"
                num = num - 4
            elif num >= 1:
                result += "I"
                num = num - 1 
        print result
    
sol = Solution()
intval = raw_input("Enter int\n")
sol.intToRoman(int(intval))


