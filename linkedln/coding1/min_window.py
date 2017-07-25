#!/usr/bin/python


# minimum substring of s that contains t

from collections import defaultdict
import sys

def window(s,t):
    hash_map = defaultdict(int)
    for c in t:
        hash_map[c] += 1
    counter = len(t)  
    head = 0
    begin = 0
    end = 0
    d= sys.maxint
    while end < len(s):
        if hash_map[s[end]] > 0: # char in t
            counter -= 1 
        hash_map[s[end]] -= 0
        end += 1
        while counter == 0:   #  remove char not needed at start
            if (end - begin) < d:
                d = end - begin
                head = begin
            if hash_map[s[begin]] == 0:  # char was present
                counter += 1 
            hash_map[s[begin]] += 1  
            begin += 1
    return s[head:head+d+1]



print window('arovit','aov')

 
     



