#!/usr/bin/python

# type('strn') -> str
# type(8) -> int
# type({}) -> dict
# type(object) -> __main__.Class

# type(int) -> type 
# type(float) -> type 
# type(str) -> type 
# type(Class) -> type   ## If class are derived from object

# New class can be created using 'type'
# type('Myclass', (), **kwargs)
# type('Myclass', (), **kwargs)

def make_myclass(**kwargs):
    return type('Myclass', (), kwargs)   # kwargs become class variables 

myclass = make_myclass(a=5,b=6) ## class object

class Myclass(object):
    var = None 
    def __init__(self):
        pass
# same as
type('Myclass', (object,), {'var':None})


class MyMetaClass(type):
    def __new__(self, cls, bases, dicta):  ## new class not object
        print self
        print "Do something before allocating memory for class"
        return super(MyMetaClass, self).__new__(self, cls, bases, dicta)
    def __init__(self, cls, bases, dicta):
        print self  
        print "initializing class"
        return super(MyMetaClass, self).__init__(cls, bases, dicta)


class SingleClass(object):
    __metaclass__= MyMetaClass
    def foo(self, param):
        print self.param

class NewMetaClass(type):
    def __call__(class_name,*base_class,**kwarg):
        print "%s %s %s"%(class_name, ",".join(base_class), kwarg)
        return type(class_name,*base_class,**kwarg)  ## or type.__call__(....)

    def __init__(self, cls, bases, dicta):
        print self  
        print "initializing second meta class"
        return super(NewMetaClass, self).__init__(cls, bases, dicta)

class MySecondclass(object):
    __metaclass__ = NewMetaClass
    def __init__(self):
        print "initializing my second class object"



from abc import ABCMeta, abstractmethod


class UserAbstract(object):
    """ User defined abstract class """
    __metaclass__ = ABCMeta
   
    @abstractmethod
    def implementthis():
        """ to be implemented """ 


class InheritUserABS(UserAbstract):
    def implementthis():
        pass


InheritUserABS()

