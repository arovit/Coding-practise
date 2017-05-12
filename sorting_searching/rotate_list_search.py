#!/usr/bin/python

rlist = [11,23,45,67,1,2,3,4,5,6,7,8,9,10]


def rotated_search(ilist, min, max, target):
    print ilist[min:max+1]
    if min > max:
        return False
    middle = (max - min)// 2
    if ilist[middle] == target:
        return True
    if ilist[max] == target:
        return True 
    if ilist[min] == target:
        return True 
    if target > ilist[middle]:
        if (ilist[middle] < ilist[max]) and (target < ilist[max]):  # right is sorted
            return rotated_search(ilist, middle+1, max, target)
        else: 
            return rotated_search(ilist, min, middle-1, target)
    elif target < ilist[middle]:
        if (ilist[middle] > ilist[min]) and (target > ilist[min]):  # lwft is sorted
            return rotated_search(ilist, min, middle-1, target)
        else: 
            return rotated_search(ilist, middle+1, max, target)
    else:
        return True


print rotated_search(rlist,0, len(rlist)-1, 45) 
