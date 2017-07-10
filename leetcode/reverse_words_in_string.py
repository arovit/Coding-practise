#!/usr/bin/python


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.strip().split(' ')
        slist = filter(lambda x:x, slist)
        rlist = self.reverseList(slist)
        return ' '.join(rlist)
        
    def reverseList(self, slist):
        for i in range(len(slist)/2):
            slist[i], slist[len(slist)-1-i] = slist[len(slist)-1-i], slist[i]
        return slist
        

