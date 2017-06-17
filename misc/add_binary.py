#!/usr/bin/python

a = 1
b = 4

def add(a,b):
    if b == 0:
        return a 
    a = a ^ b
    b = (a & b) << 1
    return add(a, b) 


add(a, b)
