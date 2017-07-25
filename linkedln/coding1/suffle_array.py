#!/usr/bin/python


def shuffle_list(alist, index):
    if index == 0:
        return
    shuffle_list(alist, index-1)
    k = random.randint(0,index)
    # swap index with k
    alist[k], alist[index] = alist[index], alist[k]

