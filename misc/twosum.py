#!/usr/bin/python



def twoSum(list_values, sum):
    """ Two sum """    
    hash_values = {}
    for i in list_values: #O(n)
        hash_values[i] = hash_values.get(i,0)+1 
        if sum-i in hash_values:
            print "%s %s"%(sum-i, i)



def twoSumBS(list_values, sum):
    """ Using binary Search """
    list_values.sort()
    for i in list_values:
        index = binarySearch(list_values, 0, len(list_values), sum-i) 
        if index != None:
            print "%s %s"%(sum-i,i) 


def binarySearch(list_values, low, high, target):
    if low > high:
        return
    middle = (low+high)/2
    if list_values[middle] > target:
        return binarySearch(list_values, low, middle-1, target)    
    elif list_values[middle] < target:
        return binarySearch(list_values, middle, high-1, target)    
    else:
        return middle  


a = [1,2,4,3,2,45,6,6,4,3,8,8,9,11,13,23,12,45,16]
twoSumBS(a,6)  

    
        
