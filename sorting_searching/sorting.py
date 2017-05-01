#!/usr/bin/python

import time


def timeit(func):
    def wrapper(slist):
        st_time = time.time()
        func(slist)
        ed_time = time.time()
        ttaken = ed_time - st_time
        print "Time taken by %s: %s secs"%(func, ttaken)
    return wrapper

@timeit
def bubble_sort(slist):
    """ Bubble sort implementation """
    for i in range(len(slist)):
        for j in range(len(slist)-i):
            if j < len(slist)-1:
                if slist[j] > slist[j+1]:
                    slist[j], slist[j+1] = slist[j+1], slist[j]
    print slist


@timeit
def selection_sort(slist):
    """ Selection sort """
    for i in range(len(slist)):
        for j in range(i+1, len(slist)):
            if slist[j] < slist[i]:
                slist[i], slist[j] = slist[j], slist[i]
    print slist

@timeit
def insertion_sort(slist):
    """ Selection sort """
    for i in range(len(slist)):
        for j in range(0,i):
            if slist[j] > slist[i]:
                slist.insert(j, slist[i])
                del slist[i]
    print slist


#slist = [1,2,3,4,5,6,7,8,9]*500
#bubble_sort(slist)
slist = [21,1,18,12,9,7,71,81,9]*1
print slist
insertion_sort(slist)
