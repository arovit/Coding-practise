#!/usr/bin/python

from os.path import join

class CustomObject(object):
    def __init__(self):
        """ Called by new upon object creation """
        self.__private = "test"
     
    def __del__(self):
        """ Called by GC at the time of garbage collectoin (not creation) """
        pass

    # comparison operator - more __lt__, __gt__
    def __cmp__(self, other):
        """ -1 if self < other, 0 if ==, 1 if self > other """
        pass

    # arithemetic operator   
    def __add__(self, other): 
        """ To add two instance using arithmetic add """
        pass

    def __radd__(self, other):
        """ To reflective add two instance using arithmetic add """
        pass

    def __iadd__(self, other):
        """ For augumented addition using arithmetic add """
        pass

    def __mul__(self, other):
        """ To multiply two instances """
        pass

    # representing instance
    def __int__(self):
        """ For type conversion to int """ # int(instance)
        pass

    def __str__(self):
        """ For type conversion to int """ # int(instance)
        pass

    def __repr__(self):
        """ For type conversion to machine readble """ # int(instance)
        pass

    def __hash__(self):
        """ hash function - used for hashing of user defined objects """
        pass

    def __sizeof__(self):
        """ Defines behaviour of sys.getsizeof() on your instance """ 
        pass

    def __getattr__(self, attribute):
        """ Get the attribute from the instance. *ONLY* called when attribute doesn't exists """     
        # MAY be do some computation
        pass

    def __getattribute__(self, attribute):
        """ get attribute from the instance. This is called unconditionally """
        print self.test

    def __setattr__(self, attribute, value):
        """ set attribute """
        #print attribute
        pass

co = CustomObject()
co.test = 1
co.test
