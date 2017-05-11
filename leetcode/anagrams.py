#!/usr/bin/python

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        form_hash = {}
        result_list = []
        for i in strs:
            default_val = form_hash.get(tuple(sorted(i)),None)
            if default_val is None:
                form_hash[tuple(sorted(i))] = [i]   
            else:
                default_val.append(i)
        map(lambda x: result_list.append(form_hash[x]), form_hash.keys())
        return result_list



sol = Solution()
print sol.groupAnagrams(['',''])
