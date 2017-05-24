#!/usr/bin/python

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap_list = []
        import heapq
        for index, i in enumerate(nums):
            if len(heap_list) < k:  # if the heap is small than k
                heapq.heappush(heap_list, i)
            elif i > heap_list[0]:  # if i is greator than min in heap is greator
                heapq.heappop(heap_list)
                heapq.heappush(heap_list, i)
            elif i < heap_list[0]:  # if i is less than min in heap - do nothing
                pass 
        return heapq.heappop(heap_list)    



