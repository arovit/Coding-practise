#!/usr/bin/python

alist = [[1,2,3],1,[12,[12,1]]]
def depth_sum(alist, rev=False):
    """ Get the depth sum of given list
    inp  : list of nested lists
    rtype: int
    """
    if not rev:
        tsum = recursive_summer(alist, 0)
    else:
        height = get_max_depth(alist)
        tsum = recursive_summer_rev(alist, height)
    return tsum

def recursive_summer(ele, level):
    sum = 0
    if type(ele) == list:
        for i in ele:
            sum += recursive_summer(i,level+1)
        return sum
    else: 
        return ele*level           

def get_max_depth(alist):
    if type(alist) != list:
        return 1 
    maxdepth = 0
    for i in alist:
       temp = get_max_depth(i)
       if temp > maxdepth:
           maxdepth = temp
    return maxdepth + 1

def recursive_summer_rev(ele, level):
    sum = 0
    if type(ele) == list:
        for i in ele:
            sum += recursive_summer_rev(i, level-1)
        return sum
    else:
        return ele*level    

def max_continous_sub_sequence_sum(alist):
    max_sum = alist[0]
    run_sum = 0
    for i in alist:
        run_sum += i
        if run_sum < 0:
            run_sum = 0
        else:
            max_sum = max(run_sum, max_sum) 
    return max_sum 

def max_continous_sub_sequence_product(alist):
    max_product = 1
    current_min_product = 1
    current_max_product = 1
    for i in alist:
        if i > 0:  # if positive
            current_min_product = min(current_min_product * i, 1)
            current_max_product = current_max_product * i
        elif i < 0:  # if negative 
            temp = current_max_product
            current_max_product = max(current_min_product * i, current_max_product)
            current_min_product = temp * i
        else:
            current_min_product = 1
            current_min_product = 1
        if current_max_product > max_product:
            max_product = current_max_product
    return max_product  


def insertion_into_sorted_range(alist, ele):
    # binary search for ele-1 or ele+1  
    # insert at that index 
    toinsert = lookPosition(start, end, alist, ele)
    for index, value in enumerate(alist):
        if index == toinsert:
            prev = alist[index]
            alist[toinsert] = ele
        elif index > toinsert:
            temp = alist[index]
            alist[index] = prev
            prev = temp 


def lookPosition(start, end, alist, target):
    if start >= end:
        if start == 0:
            return 0
        elif alist[start] > target:
            return start - 1
        elif alist[start] < target:
            return start
    middle = (end - start)/2
    if alist[middle] == ele: 
        return middle
    elif alist[middle] < ele:
        return lookPosition(middle+1, end, alist, target)
    elif alist[middle] > ele:
        return lookPosition(start, middle-1, alist, target)
        

def word_distance(word1, word2, wordlist):
    min_dist = len(wordlist)
    index1 = -1
    index2 = -1
    for index,value in enumerate(wordlist):
        if value == word1:
            index1 = index
            if index1 != -1 and index2 != -1:
                min_dist = min(abs(index1-index2), min_dist)
        elif value == word2:
            index2 = index
            if index1 != -1 and index2 != -1:
                min_dist = min(abs(index1-index2), min_dist)
    return min_dist 
    

import heapq
class RetainBestCache(object):
    def __init__(self, datasource, cachesize):
        self.datasource = datasource
        self.cache = {}
        self.keys = [] 
        self.maxlimit = cachesize
    
    def get(self, key):
        if key in self.cache:
            return self.cache[key] 
        else:
            value, rank = self.datasource.get(key) 
            self.add(key,value,rank)
            return value

    def add(self, key, value, rank):
        if len(self.cache.keys()) < self.maxlimit:
            self.cache[key] = value 
            heapq.heappush(self.keys, (rank, key)) 
        else:  # cache is full
            self.remove() 

    def remove(self):
        key = headpop(self.keys)[1]
        del self.cache[key]


def foursum(alist, target):
    results = [] 
    N_sum(alist, target, 4, [], results) 

def two_sum(alist, target):
    rlists = []
    hash_num = {}
    for i in alist:
        hash_num[i] = 1
        if (target-i) in hash_num:
            rlists.append((i, target-i))
    return rlists 

def N_sum(alist, target, N, result, results):
    if N > 2:
        for index in range(len(alist)-N+1):
            N_sum(alist[index+1:], target-alist[index], N-1, result + [alist[index]], results)
    elif N == 2:
        res = two_sum(alist, target)
        for i in res:
            result = result + [i[0], i[1]]
            results.append(result)
 
alist = [1, 0, -1, 0, -2, 2] 
foursum(alist, 0)
        
