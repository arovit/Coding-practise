#!/usr/bin/python

def find_permutations(prefix, strn):
    if not strn:
        print prefix
        return
    for i in range(len(strn)):
        find_permutations(prefix+strn[i], strn[:i]+strn[i+1:])


find_permutations('', 'abc')
