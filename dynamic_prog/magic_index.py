#!/usr/bin/python

def find_magic_index(array, start, end, mlist):
    print "start %s end %s "%(start, end)
    if not (start < end):
        return
    mindex = (end - start)/2 
    if mindex == 0:
        return 
    else:
        mindex += start 
    if array[mindex] > mindex:
        find_magic_index(array, start, mindex, mlist)
    elif array[mindex] < mindex:
        find_magic_index(array, mindex, end, mlist)
    else:
        mlist.append(mindex)
        find_magic_index(array, start, mindex, mlist)
        find_magic_index(array, mindex, end, mlist)
     
array = map(int, raw_input("Enter the array ").strip().split(' '))
magic_list = []
find_magic_index(array, 0, len(array), magic_list)
print magic_list 
