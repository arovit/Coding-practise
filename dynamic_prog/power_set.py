#!/usr/bin/python

def power_set(n):
    if n == 1:
        return ['1','']
    res = power_set(n-1)
    newres = []
    for i in res:
        newres.append(i)
        newres.append(i+'%s'%n)
    return newres


out = power_set(4)
print out
print len(out)
