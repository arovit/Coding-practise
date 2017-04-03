#!/usr/bin/python

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cindex = 0 
        common_pre = ""
        if len(strs) == 1:
            return strs[0]
        while strs:
            var = ""
            for i in range(len(strs)-1):
                if cindex < len(strs[i]) and cindex < len(strs[i+1]):
                    if not (strs[i][cindex] == strs[i+1][cindex]):
                        return common_pre
                    elif not var:
                        var = strs[i][cindex]
                else:
                    return common_pre
            if var: 
                common_pre = common_pre + var
            cindex = cindex + 1
        return common_pre


lines = raw_input()
list_str = lines.split(' ')
sol = Solution()
print sol.longestCommonPrefix(list_str)
