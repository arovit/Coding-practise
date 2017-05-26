#!/usr/bin/python

# Construct rand7 from rand5   
# That means all numbers from 0,1,2,3,4,5,6 have equal probability
# If you run rand7 the probability will be 1/7th for 0,1,2,3,4,5,6

import random

def rand5():
    return random.randint(0,4)

def constructRand7FromRand5():
    while True:
        rnum = 5*rand5() + rand5()  # (0) 1 2 3 4 (5) 6 7 8 9 (10).... 24  Find a range x*range(x) + range(x) 
        if rnum < 21:
            return rnum%7 
      

def constructRand7(seed=0):
    ## Random (X+1) =  (AX + B) mod M
    a = 92838472910  
    b = 124745 
    while True:
        seed = (a*seed + b)%7 
        yield seed  


for i in constructRand7():
    print i
