#!/usr/bin/python

a = [1,21,9,11]
max_seq_length = 0
def longest_sub_sequence(a, length):
    global max_seq_length
    if length == 1:
        return 1    
    current_length = 1
    for i in range(length-1):   # List could be ending at any element < length-1
        sublen = longest_sub_sequence(a, i)    
        if a[length-1] > a[i]:
            if sublen + 1 > current_length:
                current_length = sublen + 1  
    if current_length > max_seq_length:
        max_seq_length = current_length
    return current_length 



def longest_sub_sequence_dp(a, length):
    dpmatrix = [1 for i in range(length)]  # min length is 1
    for i in range(1,length):
        for j in range(i):
            if a[j] < a[i] and dpmatrix[i] < dpmatrix[j]+1:
                dpmatrix[i] = dpmatrix[j]+1         
    print dpmatrix
    return max(dpmatrix)


arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr) 
print longest_sub_sequence_dp(arr, n)

