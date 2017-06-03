#!/usr/bin/python

list_values = [-12,1,2,3,-1,2,-7]
def find_max_sub_sequence_sum(list_values):
    subarray = [] 
    run_sum  = 0
    max_sum  = list_values[0]
    for indx, i in enumerate(list_values):
        run_sum += i
        if run_sum > max_sum:
            max_sum = run_sum 
        elif run_sum < 0:
            run_sum = 0
    print max_sum
    print subarray
        
def find_max_sub_sequence_product(list_values):
    max_ending_here = 1
    min_ending_here = 1
    max_product = 1
    for i in list_values:
        if i > 0:  # positive
            max_ending_here = max_ending_here * i
            min_ending_here = min_ending_here * i
        elif i < 0: # negative
            temp = max_ending_here 
            max_ending_here = min_ending_here * i
            min_ending_here = temp * i
        else:  #zero
            max_ending_here = 1
            min_ending_here = 1
        if max_ending_here > max_product:
            max_product = max_ending_here
    print max_product

find_max_sub_sequence_product(list_values)


