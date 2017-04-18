#!/usr/bin/python

# Child can only take 1, 2 or 3 steps 

def num_of_ways_to_climb_stairs(n):
    """ The num of ways to climb stairs """
    if n == 3:
        return 4
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    a = num_of_ways_to_climb_stairs(n-1)
    b = num_of_ways_to_climb_stairs(n-2)
    c = num_of_ways_to_climb_stairs(n-3)
    return a + b + c


print num_of_ways_to_climb_stairs(4)
