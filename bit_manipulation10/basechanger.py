#!/usr/bin/python

class Converter(object):
    """ Any type to Any type """ 
    def __init__(self, frombase, tobase):
        self.from_base = frombase
        self.to_base   = tobase

    def change_base():
        pass ## leave the conversion


class ToBinary(Converter):
    """ Convert to Binary """
    def __init__(self, *args):
        super(ToBinary, self).__init__(*args)

    def change_base(self, num):
        stack_rem = []
        while num:
            rem = str(num%2) 
            stack_rem.append(rem)
            num = num/2 
        return "".join(stack_rem[::-1]) 


bin = ToBinary(10, 2)
print bin.change_base(5)
