#!/usr/bin/python


class BitVector(object):
    def __init__(self, max_int):
        self.byte_array = []
        number_of_ints = max_int // 32  # considering each int takes 32 bits
        if not (max_int % 32 == 0):
            number_of_ints = number_of_ints + 1 
        for i in range(number_of_ints): self.byte_array.append(0) 
        
    def setBit(number):
        dindex = number // 32
        bindex = number % 32 # or ( number & 11111 ) 
        temp_number = 1 << bindex
        self.byte_array[dindex] = self.byte_array[dindex] | self 


