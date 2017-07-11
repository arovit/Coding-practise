#!/usr/bin/python

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        word1 = s
        word2 = t
        already_mapped = set()
        if len(word1) != len(word2):
            return False
        hashw = {}
        for i in range(len(word1)):
            if word1[i] in hashw: #O(1) seen 
                if (hashw[word1[i]] != word2[i]):
                    return False
            else:
                if word2[i] in already_mapped:
                    return False
                hashw[word1[i]] = word2[i]
                already_mapped.update(word2[i])
            #print hashw
        return True
