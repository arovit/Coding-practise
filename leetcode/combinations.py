#!/usr/bin/python

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.get_all_combinations(n,k)
    
    def get_all_combinations(self, n, k):
        if k == 1:
            return [[i] for i in range(1,n+1)]
        elif k == n:
            return [[i for i in range(1,n+1)]]
        else:
            tmp = self.get_all_combinations(n-1, k)
            clist = self.get_all_combinations(n-1, k-1)
            for i in clist:
                i.append(n)
            tmp += clist
            return tmp
                    
