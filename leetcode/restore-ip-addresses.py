#!/usr/bin/python



class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.list_all_ips = []
        self.generateIP(s, 1, [])
        return self.list_all_ips

    def generateIP(self, s, count, ip_list):
        if count == 4:
            if s and s[0] == '0' and len(s) > 1:
                return     
            if s == '' or len(s) > 3 or int(s) > 255 : 
                return
            else:
                ip_list.append(s)
                self.list_all_ips.append(".".join(ip_list))
                return
        elif not s:
                return
        if s[0] == '0':
            ip_list.append('0')
            self.generateIP(s[1:], count+1, ip_list[:])
        else:
            for i in range(1,4):
                if int(s[0:i]) <= 255:
                    self.generateIP(s[i:], count+1, ip_list+[s[0:i]])
                else:
                    break


sol = Solution()
s = "25525511135"
print sol.restoreIpAddresses(s)
