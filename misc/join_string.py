#!/depot/Python-2.7/bin/python

import string
import timeit

BLENGTH = 9999999

def generate_hugelist():
    hugelist = []
    astring = string.ascii_uppercase
    hugelist.append(astring)
    hugelist = hugelist * BLENGTH
    return hugelist  

def concat_strings_in_list(slist):
    finalstring = ""
    for i in slist:
        finalstring = finalstring + i 
    return finalstring

def join_strings_in_list(slist):
    finalstring = " ".join(slist) 
    return finalstring


biglist = generate_hugelist()
concat_strings_in_list(biglist)
join_strings_in_list(biglist)
