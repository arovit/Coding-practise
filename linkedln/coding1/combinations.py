#!/usr/bin/python


def combination(elements, k):
    if k == 1:
        return [[i] for i in elements]
    elif k == len(elements):
        return [elements]
    else:  # first thing is to generate for k-1, elements-1
        tmp = combination(elements[:-1], k)
        result = combination(elements[:-1], k-1) 
        for res in result: # res is list
            res.append(elements[-1])
        return tmp + result



print combination(['a','b','c'], 2)
