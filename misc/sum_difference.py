#!/usr/bin/python

# given two array A and B
# find the elements need to be swapped such that sum(A) = sum(B) 
# sumA - a + b = sumB -b + a
# (sumA - sumB)/2 = a-b
# diff = a - b  
# b = a - diff


def findElements(array1, array2):
    S1 = sum(array1)
    S2 = sum(array2)
    hashS1 = {}
    hashS2 = {}
    diff = S1 - S2
    if diff%2 != 0:
        return None  ## No such ele exists, else can be swapped
    diff = diff/2
    map(lambda x:hashS1.update({x:1}), array1) 
    map(lambda x:hashS2.update({x:1}), array2)
    for i in array1:
        if (i - diff) in hashS2:
            return i, i-diff
     

array1 = [4,1,2,1,1,2]  # 11 - 13
array2 = [3,6,3,3]      # 15 - 13
print findElements(array2, array1)
