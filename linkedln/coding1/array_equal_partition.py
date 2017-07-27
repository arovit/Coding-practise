#!/usr/bin/python

# inp = [1,5,11,1,5,1]

# output - [[1,5,5,1],[11,1]]


def partition_array(inp):
    if sum(inp) % 2 == 1:
        return False 
    result = do_partition([],inp)
    print result
    

def do_partition(inp1, inp2):
    if sum(inp1) == sum(inp2):
        print inp1, inp2
        return True
    else:
        # pick one from inp2 add to inp1
        for i in range(len(inp2)):
            equal_set = do_partition(inp1+[inp2[i]], inp2[:i]+inp2[i+1:])        
            if equal_set:
                break
        else:
            return False  
        return True

inp = [1,5,11,1,5,1]
partition_array(inp)
