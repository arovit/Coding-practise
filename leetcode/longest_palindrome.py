#!/usr/bin/python

class String:
    def __init__(self, temp):
        self.data = temp
        h = w = len(temp) 
        self.palinar = [ [0 for i in range(w)] for j in range(h) ]
        self.maxlen = 0
      
    def find_longest_palindrome(self):
        for i in range(0, len(self.data)):    ## single char is a palindrome
            self.palinar[i][i] = 1     
            self.maxlen = 1

        for i in range(0, len(self.data)-1):  ## check two consecutive chars
            if self.data[i] == self.data[i+1]:
               self.palinar[i][i+1] = 1 
               self.maxlen = 2
               
         
        for i in range(0, len(self.data)-1):    ## Now run a O(N2) loop - if (i+1) and (j-1) is pali
            for j in range(i+1, len(self.data)):
                if self.data[i+1][j-1] and (self.data[i] == self.data[j]):
                    plen = j - i + 1 
                    if plen > self.maxlen:
                        self.maxlen = plen  
            
       

temp = String("arovit") 
temp.find_longest_palindrome()
