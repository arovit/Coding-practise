#!/usr/bin/python


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        first_index = -1  
        check_len = len(needle)
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and ( i+(check_len-1) < len(haystack) ):
                for j in range(1,len(needle)):
                    if needle[j] != haystack[i+j]:
                        break
                else:
                    first_index = i
                    return first_index
        return first_index


sol = Solution()
str1 = raw_input("Haystack").strip() 
str2 = raw_input("Needle").strip() 
print sol.strStr(str1,str2)
