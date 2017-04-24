#!/usr/bin/python

import time

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        temp = a + b
        a = b
        b = temp
for i in fibonacci():
    time.sleep(1)
    print i
