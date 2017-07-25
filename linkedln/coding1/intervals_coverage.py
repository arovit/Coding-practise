#!/usr/bin/python

import sys
intervals = [(0,6),(4,7)]


def intervals_coverage(intervals):
    sorted_invls = sorted(intervals, key=lambda x:x[0])
    print sorted_invls
    sum = 0
    l = sorted_invls[0][0]
    r = sorted_invls[0][1]
    sum = 0
    sorted_invls.append((sys.maxint, sys.maxint)) 
    for i in range(1,len(sorted_invls)):
        if r > sorted_invls[i][0]:  # previous r is more
            if r < sorted_invls[i][1]: # r less than new r = pverlapping is there     
                r = sorted_invls[i][1]
            elif r > sorted_invls[i][1]: # r more than new r = it is contained   
                pass
        elif r < sorted_invls[i][0]: # previour r was smaller
            sum += r-l
            l = sorted_invls[i][0]
            r = sorted_invls[i][1] 
    return sum    


print intervals_coverage(intervals)
