#!/usr/bin/python


class BitVector(object):
    def __init__(self, max_value):
        self.max_index= max_value >> 5   ## Divide by 32 - 8*4
        if self.max_index:
            self.bit_vector = [0] * self.max_index
        else:
            self.bit_vector = [0]
    
    def getBit(self, bit_index):
        word_number = bit_index >> 5     ## Divide by 32
        bit_number = bit_index & 0x1F    ## Mode 32 - only bit 1111 (1-31) are 1
        bitval =  (self.bit_vector[word_number] & (1 << bit_number))
        return bitval != 0    ## Mask the word with all zero's except bit number

    def setBit(self, bit_index):
        word_number = bit_index >> 5     ## Divide by 32
        bit_number = bit_index & 0x1F    ## Mode 32 - only bit 1111 (1-31) are 1
        self.bit_vector[word_number] =( self.bit_vector[word_number] | (1 << bit_number))

    def __str__(self):
        return "%s"%self.bit_vector


bv = BitVector(16)
bv.setBit(4)
bv.setBit(2)
print bv
