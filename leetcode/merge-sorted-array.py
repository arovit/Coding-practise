#!/usr//bin/python 

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i1 = i2 = o1 = 0
        while o1 < m and i2 < n:
            if nums1[i1] >= nums2[i2]:
                nums1.insert(i1,nums2[i2])
                i1 += 1
                i2 += 1
            else:
                o1 += 1
                i1 += 1
        if o1 == m: # array 1 is exhasted , take from array 2
            nums1[i1:] = nums2[i2:n]
        elif i2 == n: # array 2 is exhasted, take element only from array 1
            nums1[i1:] = nums1[i1:m-o1+1] 

sol = Solution()
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
sol.merge(nums1, m, nums2, n)
print nums1
