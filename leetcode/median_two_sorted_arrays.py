#!/usr/bin/python

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not (nums1  or nums2):
            return ""
        self.mergeArrays(nums1, nums2)
        if len(nums1) %2 == 1:
            median = nums1[len(nums1)/2]
        else:
            between = len(nums1)/2
            median = (nums1[between] + nums1[between-1])/2.0
        print median
        return median 

    def mergeArrays(self, array1, array2):
        """
        array1: list
        array2: list
        rtype: None, array1 is modified in place
        """
        i = 0 
        j = 0
        while (i<len(array1) and  j<len(array2)):
            if array1[i] >= array2[j]:
                ele = array2.pop(j)
                array1.insert(i,ele)
            else:
                i = i + 1 
        if i == len(array1):
            array1.extend(array2)
     

solver = Solution()
"""
array1 = raw_input("Enter the first array").strip().split(' ')
if array1:
    array1 = map(int, array1)
else:
    array1 = [] 
array2 = raw_input("Enter the second array").strip().split(' ')
if array2:
    array2 = map(int, array2)
else:
    array2 = [] 
"""
solver.findMedianSortedArrays([], [3,4,9])
