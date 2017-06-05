#!/usr/bin/python


class MasterMind(object):
    def __init__(self):
        self.slots = None # eg. RGYB
        self.slots_len = 0
        self.color_count = {}
        
    def read_slots(self):
        self.slots = "RGYB" # set to anything. or randomize
        self.slots_len = len(self.slots)
        for i in self.slots:
            self.color_count[i] = self.color_count.get(i,0) + 1  
        
    def guess(self, guess):
        hits = 0
        phits = 0
        ignore_indexes = {}
        for i in range(self.slots_len):
            if self.slots[i] == guess[i]:
                hits += 1 
                self.color_count[guess[i]] -= 1  # remove colors that are same
                ignore_indexes.update({i:1})
           
        for i in range(self.slots_len):
            if i in ignore_indexes:
                continue
            if guess[i] in self.color_count:
                phits += 1
                self.color_count[guess[i]] -= 1  # remove colors that are same
                if self.color_count[guess[i]] < 1:
                    del self.color_count[guess[i]] 
        return hits, phits


mm = MasterMind()
mm.read_slots()
print mm.guess("RBBY")
