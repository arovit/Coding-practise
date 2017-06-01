#!/usr/bin/python

# length | 1 | 2 | 3
# price  | 5 | 8 | 2

# given 'n' inches 


def get_max_possible(n, price): #price[0] = 0
   #  n , n-1(index) + 1(index), n-2 
    max_val = 0  
    for i in range(1, n+1):
        max_val = max(get_max_possible(price[n-i]) + price[i], max_val) 
    return max_val   


