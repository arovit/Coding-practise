#!/usr/bin/python

## Total number of boards K
## Shorter Board len short
## Longer Board len long



def getAllLengths(total, count, short, long, visited):
    key = "%s#%s"%(total, count)
    if key in visited:
        return
    if count == 0:
        print total
    else:
        getAllLengths(total+short, count - 1, short, long, visited)   
        getAllLengths(total+long, count - 1, short, long, visited)   
        visited[key]=1

#getAllLengths(0, 3, 1, 2, {})



def getDistintSum(short, long, count):
    for i in range(count): # i - number of short
        num_short = i
        num_long = count -i
        sum = num_short*short + num_long*long 
        print sum 

getDistintSum(1,2,3)       

