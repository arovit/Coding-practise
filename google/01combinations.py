#!/usr/bin/python

def produce(cstring):
    if "?" in cstring:
        fi = cstring.index('?')
        produce(cstring[:fi] + "0" + cstring[fi+1:])
        produce(cstring[:fi] + "1" + cstring[fi+1:])
    else:
        print cstring 

produce("1?")





