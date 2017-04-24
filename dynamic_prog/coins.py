#!/usr/bin/python


# Infinite number of 25 cents, 10 cents, 5 cent, 1 cent. 

def generate_ways(n, currencylist, index):  ## generate number of ways for n cent
    if index == len(currencylist)-1:
        return 1
    currency = currencylist[index]
    i = 0
    totnum = n
    ways = 0
    while totnum >= 0 :
        ways = ways + generate_ways(totnum, currencylist, index+1)
        i += 1 
        totnum = n - (i * currency)
    return ways

n = input("Enter the n cent ")
print generate_ways(n, [25, 10, 5, 1], 0)
