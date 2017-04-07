#! /usr/bin/python

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_code = { '(': 1, ')': 1, '{': 2, '}':2, '[':3, ']':3 }
        opening = "({["
        closing = ")}]"
        paran = []
        for i in s:
            if i in opening:
                 paran.append(i)
            elif i in closing:
                if not paran:
                    return False
                last_symbol = paran.pop()
                if hash_code[i] != hash_code[last_symbol]:
                    return False
            
        if paran:
            return False
        else:
            return True

