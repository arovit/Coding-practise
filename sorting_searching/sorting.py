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
    #print slist


@timeit
def selection_sort(slist):
    """ Selection sort """
    for i in range(len(slist)):
        for j in range(i+1, len(slist)):
            if slist[j] < slist[i]:
                slist[i], slist[j] = slist[j], slist[i]
    #print slist

@timeit
def insertion_sort(slist):
    """ Selection sort """
    for i in range(len(slist)):
        for j in range(0,i):
            if slist[j] > slist[i]:
                slist.insert(j, slist[i])
                del slist[i+1]
    #print slist


@timeit
def merge_sort_wrapper(slist):
    """ Wrapper for merge sort """
    #print merge_sort(slist) 

def merge_sort(slist):
    """ Merge sort """
    if not slist:
        return []
    elif len(slist) == 1: 
        return slist
    else:
        middle = len(slist)//2 
        leftarray = merge_sort(slist[:middle])
        rightarray = merge_sort(slist[middle:])
        mergedarray = mergetwoarray(leftarray, rightarray) 
        return mergedarray
 
def mergetwoarray(larray, rarray):
    newarray = []
    i = 0
    j = 0 
    while (i < len(larray)) and (j < len(rarray)):
        print larray[i] < rarray[j]
        if larray[i] < rarray[j]:
            newarray.append(larray[i])
            i += 1
        elif larray[i] >= rarray[j]:
            newarray.append(rarray[j])
            j += 1 
    if i == len(larray):
        newarray.extend(rarray[j:]) 
    elif j == len(rarray):
        newarray.extend(larray[i:]) 
    return newarray


def quicksort(array, lo, hi): 
    if lo < hi:
        p = partition_sort(array, lo, hi)
        quicksort(array, lo, p-1)
        quicksort(array, p+1, hi)

def partition_sort(array, lo, hi):
    pivot = array[lo]
    i = lo + 1
    j = hi 
    while True:
        while i <= j and array[i] <= pivot:
            i = i+1
        while i <=j and array[j] >= pivot:
            j = j-1
        if  j < i:
            break
        else:
            array[i], array[j] = array[j], array[j]
    array[lo], array[j] = array[j], array[lo]    
    return j
 
slist = [9,2,3,4,6,1,8,9,32,12,34,7,55,3]*500
bubble_sort(slist)
slist = [9,2,3,4,6,1,8,9,32,12,34,7,55,3]*500
insertion_sort(slist) 
slist = [9,2,3,4,6,1,8,9,32,12,34,7,55,3]*500
merge_sort_wrapper(slist)
slist = [9,2,3,4,6,1,8,9,32,12,34,7,55,3]*500
quicksort(slist, 0, len(slist)-1)
