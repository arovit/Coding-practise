#!/usr/bin/python

# given input
def largest_sum_subsequence(a, length):
    smatrix = [[0 for i in range(length)] for j in range(length)]
    max_sum = 0
    for i in range(length):
        smatrix[i][i] = a[i]

    for i in range(length): 
        for j in range(i+1, length):
            # for i :j, add j to i :j-1
            if smatrix[i][j] < (a[j] + smatrix[i][j-1]):
                smatrix[i][j] = a[j] + smatrix[i][j-1] 
                if smatrix[i][j] > max_sum:
                    max_sum = smatrix[i][j]  
    print max_sum


def largest_sum_subsequence_opt(a, length):
    sum = 0
    maxSum = 0
    for i in range(len(a)):
        sum += a[i]
        if sum > maxSum:
            maxSum = sum
        if sum < 0:
            sum = 0
    print maxSum

a = [2,-8,3,-2,4,-10]
largest_sum_subsequence(a,len(a))
largest_sum_subsequence_opt(a,len(a))


