#!/usr/bin/python

# input two array 
# weight
# value



def knapsack(weight, value, n, MaxW):
    if n == 0 or MaxW == 0:
        return 0 
    
    if weight[n-1] > MaxW:  # if nth element is too heavy - leave it
        return knapsack(weight, value, n-1, MaxW)
  
    ## Now decide to include nth element or not
    ## Get max_value( with_include or without_include ) 
    return max(val[n-1] + knapsack(weight, value, n-1, MaxW-weight[n-1]), knapsack(weight, value, n-1, MaxW))
     
val = [60, 100, 120]
wt = [10, 20, 30]    
print knapsack(wt, val, 3, 50)


 
