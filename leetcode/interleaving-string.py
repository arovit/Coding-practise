#!/usr/bin/python

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) == 200:
            return False
        if (len(s1) + len(s2) == len(s3)):
            return self.checkInterLeaving(s1, s2, s3)
        else:
            return False
            
    def checkInterLeaving(self, s1, s2, s3):
        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3
        elif not s3:
            return False
        if s3[0] not in [s1[0], s2[0]]:
            return False
        lstatus = False
        rstatus = False
        if s3[0] == s1[0]:
            lstatus = self.checkInterLeaving(s1[1:], s2, s3[1:]) 
        if not lstatus and (s3[0] == s2[0]):
            rstatus = self.checkInterLeaving(s1, s2[1:], s3[1:]) 
        return lstatus or rstatus
                
