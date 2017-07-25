#!/usr/bin/python



def find_influencers(imatrix):
    n = len(imatrix)  # number of people
    influ_other = [0 for i in range(n)]
    got_influ = [0 for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                influ_other[i] += 1 
                got_influ[j] += 1
            
    for i in range(n):
        if influ_other[i] == n-1 and got_influ[i] == 0:
            print "influencer %s"%i
            
