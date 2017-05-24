#!/usr/bin/python


# find number  of zeros in a given factorial


def findzeros(number):
    count = 0
    i = 5
    while i < number:
        count += number/i   # get number of numbers divisible by i 5,10,15,20,,,,,
        i = i * 5           # get increment the i
    return count 

print findzeros(15)    # 5*6*7*8*9*10*11*12*13*14*15
