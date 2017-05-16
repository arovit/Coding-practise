#!/usr/bin/python

def max(a,b):
    c = a - b  
    k = c >> 31 & 0x1  # find the sign of k
    return a - (k*c)
print max(5,9)
