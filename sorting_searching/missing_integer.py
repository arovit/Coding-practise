#!/usr/bin/python


class BitVector(object):
    def __init__(self, max_int):
        number_of_ints = max_int+1 // 32  # considering each int takes 32 bits
        if not (max_int+1 % 32 == 0):
            number_of_ints = number_of_ints + 1 
        self.byte_array = [0]*number_of_ints

    def setBit(self, number):
        dindex = number // 32
        bindex = number % 32 # or ( number & 0x1F ) 
        temp_number = 1 << bindex
        self.byte_array[dindex] = self.byte_array[dindex] | temp_number 
     
    def getBit(self, number):
        dindex = number // 32
        bindex = number % 32 # or ( number & 0x1F ) 
        temp_number = 1 << bindex
        print dindex
        return (self.byte_array[dindex] & temp_number != 0) 


bv = BitVector(64)
bv.setBit(2)
bv.setBit(4)
random_list = [1,23,34,54,23,12,33,7,8,43,45,64,64,23,23]
for i in random_list:
    if bv.getBit(i):
        print "Duplicate %s"%i
    else:
       bv.setBit(i)
