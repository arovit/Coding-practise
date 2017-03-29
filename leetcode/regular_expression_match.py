#!/usr/bin/python

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:                                    # pattern consumed 
            if s:
                return False
            else:
                return True
        else:
            if (not s) and (len(p) >= 2 and p[1] == "*"):
                return self.isMatch(s, p[2:])
            elif not s:
                return False 
 
        if len(p) == 1:
            if p[0] != '.': 
                if p[0] != s[0]:
                    return False 
                else:
                    return self.isMatch(s[1:], p[1:])
            else:
                return self.isMatch(s[1:], p[1:])
        if p[1] != '*':
            if (s[0] != p[0]) and (p[0] != '.'):     # ab*
                return False 
            elif (p[0] == '.') or (s[0] == p[0]):    # .b* 
                return self.isMatch(s[1:],p[1:]) 
        elif p[1] == '*':
            if self.isMatch(s, p[2:]):               # a*bc
                return True
            i = 0
            while i < len(s):                        # s : dddaaaabc
                print s[i], p[0]  
                if s[i] == p[0] or p[0] == ".":
                    if self.isMatch(s[i+1:], p[2:]):
                        return True  
                else:
                    return False
                i += 1
            return False

solver = Solution()
string_pat = raw_input("Enter s p\n")
string = string_pat.split(" ")[0]
pat = string_pat.split(" ")[1]
print solver.isMatch(string , pat)
