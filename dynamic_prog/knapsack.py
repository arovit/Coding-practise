#!/usr/bin/python


def return_max_value(weight, value, n, max_weight):
    if n == 0 or max_weight == 0:
        return 0
    if weight[n-1] > max_weight:  # If weight of nth is more than max_weight 
        return return_max_vale(weight, value, n-1, max_weight)    # return previous 
    
    # include  or not include ?
    val1 = value[n] + return_max_value(weight, value, n-1, max_weight-weight[n-1])
    val2 = return_max_value(weight, value, n-1, max_weight)
    return  max(val1, val2)
