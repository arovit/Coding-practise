#!/usr/bin/python

"""
    	
The old song declares "Go ahead and hate your neighbor", and the residents of Onetinville have taken those words to heart. Every resident hates his next-door neighbors on both sides. Nobody is willing to live farther away from the town's well than his neighbors, so the town has been arranged in a big circle around the well. Unfortunately, the town's well is in disrepair and needs to be restored. You have been hired to collect donations for the Save Our Well fund.

Each of the town's residents is willing to donate a certain amount, as specified in the int[] donations, which is listed in clockwise order around the well. However, nobody is willing to contribute to a fund to which his neighbor has also contributed. Next-door neighbors are always listed consecutively in donations, except that the first and last entries in donations are also for next-door neighbors. You must calculate and return the maximum amount of donations that can be collectedp

Eg. { 10, 3, 2, 5, 7, 8 }
Returns: 19

"""

def maxDonations(donation):
    max_donation = [0 for i in range(len(donation))] 
    max_donation[0] = donation[0] 
    max_donation[1] = donation[1]
    for i in range(2, len(donation)):
        for j in range(i-1):
            if (donation[i]+max_donation[j]) > max_donation[i]: 
                max_donation[i] = donation[i]+max_donation[j]
    return max_donation[-1]


def solveBadNeighbour(donation):
    a = maxDonations(donation[:-1])
    b = maxDonations(donation[1:])
    return max(a,b)

don = [ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 ] 
print solveBadNeighbour(don)


