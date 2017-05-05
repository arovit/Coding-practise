#!/usr/bin/python


def permutation(prefix, inp_string):
    if inp_string == "":
        print prefix
        return
    for i in range(len(inp_string)):
        permutation(prefix+inp_string[i],  inp_string[:i]+inp_string[i+1:])   

permutation('','abc')
