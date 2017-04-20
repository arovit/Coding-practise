#!/usr/bin/python


def permutationunique(strn):
    """ Permutation of unique chars """
    new_result = []
    if len(strn) == 2:
        new_result.append(strn)
        new_result.append(strn[::-1])
    else:
        for i in range(len(strn)):
            if i == 0:
                resultset = permutationunique(strn[i+1:])
            elif i == (len(strn) - 1):
                resultset = permutationunique(strn[:i])
            else:
                resultset = permutationunique(strn[:i] + strn[i+1:]) 
            for st in resultset:
                new_result.append(strn[i]+st)
    return new_result

