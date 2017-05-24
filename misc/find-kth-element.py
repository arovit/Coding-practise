#!/usr/bin/python

# given two sorted array, find kth index element 


def find_kth_element(list1, list2, k):
    print list1, list2, k
    if not list1:
        return list2[k] 
    if not list2:
        return list1[k]
    middle_index1 = len(list1)//2
    middle_list1 = list1[middle_index1]
    middle_index2 = len(list2)//2
    middle_list2 = list2[middle_index2]

    if k <= (middle_index1 + middle_index2):  # if k is less than middle_index1 + middle_index2 
        if middle_list1 > middle_list2:
            return find_kth_element(list1[:middle_index1], list2, k)  # second half of middle_list1 will def be not included 
        else:
            return find_kth_element(list1, list2[:middle_index2], k)  # 2nd half of list2 not included
    elif k > (middle_index1 + middle_index2):  # if k is more than middle_index1 + middle_index2 
        if middle_list1 > middle_list2:
            return find_kth_element(list1, list2[middle_index2+1:], k-middle_index2-1)  # second half of middle_list1 will def be not included 
        else:
            return find_kth_element(list1[middle_index1+1:], list2, k-middle_index1-1)  # 2nd half of list2 not included
        



#a = [1,4,6,9,10,11,14,16,19]
#b = [5,7,13,15,18,20]
a = [1,4]
b = [5]
print find_kth_element(a, b , 2)
