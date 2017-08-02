#!/usr/bin/python

# decorating func without arguements 

import time
class TimeIT(object):
    def __init__(self, func_obj):
        self.func_obj=func_obj   # at the start of execution 

    def __call__(self):
        s = time.time()
        self.func_obj()
        e = time.time()
        print "time taken %s"%(e-s)
"""
@TimeIT
def func():
    time.sleep(1)
    print "call func"
func()
"""

# decorating func with arguements 

class TimeITWithArgs(object):
    def __init__(self, func_obj):
        self.func_obj=func_obj   # at the start of execution 

    def __call__(self,*args):
        s = time.time()
        self.func_obj(*args)
        e = time.time()
        print "time taken %s"%(e-s)

"""
@TimeITWithArgs
def func(a,b,c):
    time.sleep(1)
    print "call func with %s %s %s"%(a,b,c)
func(1,2,3)
"""


# decorating func with arguements with arguements

class TimeITWithArgs(object):
    def __init__(self, arg1, arg2, arg3):   # arguements for the decorator
        self.args1 = arg1
        self.args2 = arg2
        self.args3 = arg3

    def __call__(self, f):       # Now, instead of __init__ getting func object, __call__ gets called during initilization
        def wrapper(*args):
            print "inside wrapper"
            s = time.time()
            f(*args)  # call also make use of self.arg
            e = time.time()
        return wrapper    

@TimeITWithArgs(5,6,7)
def func(a,b,c):
    time.sleep(1)
    print "call func with %s %s %s"%(a,b,c)

func(1,2,3)

