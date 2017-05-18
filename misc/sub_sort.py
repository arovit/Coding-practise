#!/usr/bin/python

# given an array, find indices of m and n such that sorted elements m-n , entire aray would be sorted
# left seq <middle> right sequence
# 1 2 3 8 4 6 7 12 34 

# ll - 3
# rf - 4

def sub_sort(array):
    """ find the sub array  """
    left_last = find_left_increasing_sequence(array)
    right_first = find_right_decresing_sequence(array)
    # expand middle
    # now in the middle segment between left_last and right_first , find min_index and max_index 
    max_index = left_last              ##
    min_index = right_first            ##
    for i in range(left_last+1, right_first):
        if array[i] > array[max_index]: max_index = i
        if array[i] < array[min_index]: min_index = i
    index1 = shrink_left(array, left_last, min_index)         
    index2 = shrink_right(array, right_first, max_index)         
    print index1, index2


def shrink_left(array, left_last, min_index):
    for i in range(left_last,-1,-1):
        if array[i] <= array[min_index]:
            break     
    return i

def shrink_right(array, right_first, max_index):
    for i in range(right_first, len(array)):
        if array[i] > array[max_index]:
            break
    return i
 
def find_left_increasing_sequence(array):
    start = 0
    while start < len(array)-1: 
        if array[start] < array[start+1]:    
            start += 1    
        else:
            break
    return start

def find_right_decresing_sequence(array):
    end = len(array)-1  
    while end > 0:
        if array[end] > array[end-1]:
            end -= 1 
        else:
            break
    return end 

sub_sort([1,2,3,8,4,6,7,12,34])
