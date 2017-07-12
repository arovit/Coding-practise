#!/usr/bin/python

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        visited = set() # to remove reduntant - need to see how redunant 
        resultant = []
        if not nums1 or not nums2:
            return resultant
        queue = [(nums1[0] + nums2[0], (0,0))]  # heap queue  start with (sum, (i,j)) 
        while queue and k:
            _, (i, j) = heapq.heappop(queue)
            resultant.append((nums1[i],nums2[j]))
            # add left and right into heapq
            if j+1 < len(nums2) and not (i,j+1) in visited:
                heapq.heappush(queue, (nums1[i]+nums2[j+1],(i,j+1)))
                visited.add((i,j+1))
            if i+1 < len(nums1) and not (i+1,j) in visited:
                heapq.heappush(queue, (nums1[i+1]+nums2[j],(i+1,j)))
                visited.add((i+1,j))
            k -= 1
        return resultant

