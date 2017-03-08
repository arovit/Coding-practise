#!/usr/bin/python

import sys
import copy
import string

class stringStream:
    def __init__(self, text): 
        self.text = text  
        #print self.text
    def setPattern(self, patrn):
        self.patrn = patrn
        #print self.patrn
    def prepareSearch(self):
        self.compare_hash = {}
        for k in string.lowercase:
            self.compare_hash[k] = 0 

    def search(self):
        """ Search for all permutations of 'patrn' in 'text'
        Trickly part is - Doing in O(n) """

        self.prepareSearch() 
        run_hash = copy.deepcopy(self.compare_hash)
        self.windowlen = len(self.patrn) 
        for i in self.patrn:
            self.compare_hash[i]+=1
        for i in range(0, (len(self.text)-self.windowlen)+1):
            if i == 0:
                for j in range(0,self.windowlen):
                    run_hash[self.text[i+j]] += 1
            else:
                newindex = i + (self.windowlen-1)
                run_hash[self.text[newindex]] += 1
            if self.compare_hash  == run_hash:
                print "Found at index %s"%i  
            #print "RUN",run_hash
            #print "COMPARE",self.compare_hash
            run_hash[self.text[i]] -= 1


if __name__ == "__main__":
    text = sys.argv[1]
    patten = sys.argv[2]
    obj = stringStream(text)    ##
    obj.setPattern(patten)
    obj.search()
