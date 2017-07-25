#!/usr/bin/python

#A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a zig-zag sequence.
#{ 1, 7, 4, 9, 2, 5 }
#Returns: 6



def find_longest_zigzag_sequence(zlist):
    zlen = len(zlist)
    pos_diff = [1 for i in range(zlen)]
    neg_diff = [1 for i in range(zlen)]
    for i in range(zlen):
        for j in range(i):
            diff = zlist[i] - zlist[j]
            if diff > 0:  # pos diff
                if pos_diff[i] < neg_diff[j]+1:
                    pos_diff[i] = neg_diff[j] + 1
            elif diff < 0: # neg
                if neg_diff[i] < pos_diff[j]+1:
                    neg_diff[i] = pos_diff[j] + 1  
    return max(max(pos_diff), max(neg_diff))

zlist = [ 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32 ]
print find_longest_zigzag_sequence(zlist)
