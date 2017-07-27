#!/usr/bin/python



def change(d, b):
    output = []
    while d > 0:
        output.insert(0, d%b)
        d = d//b
    return output


def convert(output, b):
    n = 0  
    for d in output:
        n = b * n + d
    return n


print change(20,2)
