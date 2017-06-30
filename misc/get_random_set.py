#!/usr/bin/python

import random
# get random set of intergers from given array

def get_random_set(arrayn,m):
    if len(arrayn) == m:
        return arrayn
    randset = get_random_set(arrayn[1:], m)  
    # now decide , do you want arrayn[0] in randset 
    k = random.randint(0,len(arrayn)-1)
    if k < m:
        randset[k] = arrayn[0]
    return randset


arrayn = [1,2,3,4,5]
print get_random_set(arrayn, 2)
