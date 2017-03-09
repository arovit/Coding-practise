#!/usr/bin/python

import sys
import copy
import string

## Problem to check if a string is one operation away from other string
## operation could be any of - delete, insert, rename


class stringStream:
    def __init__(self, text1, text2): 
        self.text1 = text1  
        self.text2 = text2
        self.hash1 = {}
        self.hash2 = {}
        self.constructHash(self.text1, self.hash1)
        self.constructHash(self.text2, self.hash2)

    def constructHash(self, text, hash):
        for i in text:
            hash[i] = 1 + hash.get(i,0)

    def checkOneAway(self):
        if abs(len(self.text1)-len(self.text2)) > 1:
            return "Not one step away"       
        else:
            diff = 0
            remain = 0
            if len(self.text1) < len(self.text2):
                small = self.text1
                big = self.hash2
            else:
                small = self.text2
                big = self.hash1
            for i in small:
                if (i in big.keys()) and big[i] > 0: 
                    big[i] -= 1
                else:
                    diff += 1
            for i in big.keys():
                remain += big[i]    
            if diff == remain == 1:
                return "One step away"    
            elif diff <= 1:
                return "One step away"    
            return "Not one step away" 
                   
if __name__ == "__main__":
    text1 = sys.argv[1]
    text2 = sys.argv[2]
    obj = stringStream(text1, text2)
    print obj.checkOneAway() 
