#!/usr/bin/python



def check_isomorphic(word1, word2):
    if len(word1) != len(word2):
        return False
    hashw = {}
    seen = set()
    for i in range(len(word1)):
        if word1[i] in hashw: #O(1) seen 
            if (hashw[word1[i]] != word2[i]):
                return False
        else:
            if word2[i] in seen:
                return False
            hashw[word1[i]] = word2[i]
            seen.update(word2[i])
        
            


