#!/usr/bin/python

class HashTable(object):
    def __init__(self):
        self.data_count = 0
        self.size = 100
        self.data_array = [None for i in range(self.size)]
        
    def add(self, kdata, value):
        # insert data into data_count     
        index = id(kdata) % self.size 
        if self.data_array[index] == None:
            self.data_array[index] = [(kdata, value)]
        else:
            self.data_array[index].append((kdata, value))
        self.data_count += 1
        self.resize()
 
    def resize(self):
        # check resize of array
        if self.data_count < (self.size/2):
            return 
        else: 
            self.size *= 2
        temp = self.data_array
        self.data_array = [None for i in range(self.size)] 
        self.data_count = 0 
        for kv in temp:
            if kv == None:
                continue
            else:
                for (key, value) in kv:
                    self.add(key, value)
         
    def get(self, key):
        i = id(key) % self.size
        kvs = self.data_array[i] 
        if kvs == None:
            return False 
        for k,v in kvs:
            if k == key:
                return v
        return False 


htable = HashTable()
htable.add(1,'a')
htable.add(2,'b')         
htable.add(3,'c')         
htable.add(4,'f')         
htable.add(5,'d')         
htable.add(6,'g')         
print htable.get(1)
print htable.get(2)
print htable.get(3)
print htable.get(4)
