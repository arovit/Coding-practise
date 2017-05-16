#!/usr/bin/python


def return_max_value(weight, value, n, max_weight):
    print n, max_weight
    if n == 0 or max_weight == 0:
        return 0
    if weight[n-1] > max_weight:  # If weight of nth is more than max_weight 
        return return_max_vale(weight, value, n-1, max_weight)    # return previous 
    
    # include  or not include ?
    val1 = value[n-1] + return_max_value(weight, value, n-1, max_weight-weight[n-1])
    val2 = return_max_value(weight, value, n-1, max_weight)
    return  max(val1, val2)


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print return_max_value(wt , val , n, W)

def dp_matrix_knapsack(weight, value, n, max_weight):
    dpmat = [[0 for i in range(max_weight+1)] for j in range(n+1)]
    for i in range(n+1);
        for j in range(max_weight+1):
            if i == 0 or j == 0:
                dpmat[i][j] = 0
            elif weight[i-1] > max_weight:
                dpmat[i][j] = dpmat[i-1][j]
            else:
                val1 = val[i-1] + dpmat[i-1][max_weight-j-1]
                val2 = dpmat[i-1][j]
                dpmat[i][j] = max(val1, val2)
    return dpmat[n][W]   
