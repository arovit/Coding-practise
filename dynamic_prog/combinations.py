#!/usr/bin/python

# implement combination


def combinations(string, length):
    total_stns = []
    for i in range(len(string)):
        if length == 1:
            total_stns.append(string[i])  
        else:
            for k in combinations(string[i+1:], length-1):
                total_stns.append(string[i]+k)     
    return total_stns


print combinations('arovit',3)

