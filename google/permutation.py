#!/usr/bin/python

# abc
# prefix a - bc
# prefix ab - c
# prefix ac - b

def permutation(prefix, nstring):
    if not nstring:
        print "".join(prefix)
    for i in range(len(nstring)):
        prefix.append(nstring[i])
        permutation(prefix, nstring[:i]+nstring[i+1:])
        prefix.pop()


permutation([],'abc')
