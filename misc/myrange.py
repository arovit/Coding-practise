#!/usr/bin/python


## My own implementation of class

class Range(object):
    def __init__(self, min, max=None, step=1):
        """ Constructor of range """
        self._min = min
        self._max = max
        self._step = step    
        if self._step == 0:
            raise ValueError('Step cannot be 0')
        if self._max is None:
            self._max = min
            self._min = 0
        self._length = ((self._max-self._min)+(self._step-1))//self._step
        self._cindex = -1

    def __len__(self):
        return self._length    

    def __getitem__(self, index):
        if index < 0:
            temp =  index + self._length
        else:
            temp = index
        if not (0 < temp < self._length):
            raise IndexError("Index %s out of bound"%index)
        newval = self._min + (self._step * temp)
        return newval
