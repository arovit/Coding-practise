#!/usr/bin/python


def permutationunique(strn):
    """ Permutation of unique chars """
    new_result = []
    seen = []
    if len(strn) == 2:
        new_result.append(strn)
        if strn[0] != strn[1]:
            new_result.append(strn[::-1])
    else:
        for i in range(len(strn)):
            print seen
            if strn[i] in seen:
                continue
            if i == 0:
                resultset = permutationunique(strn[i+1:])
            elif i == (len(strn) - 1):
                resultset = permutationunique(strn[:i])
            else:
                resultset = permutationunique(strn[:i] + strn[i+1:]) 
            seen.append(strn[i])
            for st in resultset:
                new_result.append(strn[i]+st)
    return new_result


strn = raw_input("Enter a string ").strip()
print permutationunique(strn)
