#!/usr/bin/python


class Solution:
    def romanToInt(self, rstring):
        symbols = {'I':1, 'V':5 , 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }           
        num = 0
        for index, val in enumerate(rstring):
            if index != len(rstring)-1:
                if symbols[rstring[index]] < symbols[rstring[index+1]]:
                    num = num - symbols[rstring[index]] 
                    continue
            num = num + symbols[rstring[index]]
        print num             

sol = Solution()
roman = raw_input("Enter roman\n")
sol.romanToInt(roman)


