#!/usr/bin/python

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.valid_ip_adressess = []
       

    def ip_address(string, count):
        if count == 3:
            if not string:
                return False
            if int(string) <= 255:
                return True
            else:
                return False 
        
        if len(string) in [1,2,3]:
            
        
