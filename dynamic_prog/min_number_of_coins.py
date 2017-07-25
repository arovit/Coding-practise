#!/usr/bin/python

# Given list of coins eg. [1,3,5,7,9]
# find min number of coins needed for a given sum S

from collections import defaultdict

def min_coins(sum_s, coins):
    min_coin_dict  = {}
    min_coin_dict[0] = 0
    for s_i in range(sum_s+1):
        for j in coins:
            if j <= s_i:
               if not s_i in min_coin_dict or (min_coin_dict[s_i] > 1+min_coin_dict[s_i-j]):
                   min_coin_dict[s_i] = 1+min_coin_dict[s_i-j]
    return min_coin_dict[sum_s]

print min_coins(11,[1,3,5])
