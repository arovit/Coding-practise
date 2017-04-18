#!/usr/bin/python


def tower_of_hanoi(nstacks,a,b,c):
    """
    Solve tower of hanoi
    """
    if nstacks > 0:
        tower_of_hanoi(nstacks-1, a, c, b)   
        if a:
            c.append(a.pop())
        tower_of_hanoi(nstacks-1, b, a, c)



a = [3,2,1]
b = []
c = []
tower_of_hanoi(3, a, b, c)
print c
