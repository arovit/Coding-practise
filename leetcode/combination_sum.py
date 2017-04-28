#!/usr/bin/python

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resultlist = []
        print self.checksum(candidates, target, 0, 0, [])
        print self.resultlist
        return self.resultlist
    
    def checksum(self, listn, tsum, index, ways, tresult):
        if tsum == 0:
            self.resultlist.append(tresult[:])
            return 1
        elif tsum < 0:
            return 0
        for i in range(index, len(listn)):
            num = listn[i]
            count = 1
            while num <= tsum:
                append_list(tresult, listn[i], count)
                if self.checksum(listn, tsum-num, i+1, ways, tresult):
                    ways += 1
                pop_list(tresult, count)
                count += 1
                num = listn[i] * count
        return ways

def append_list(lis, num, times):
    while times > 0:
        lis.append(num)
        times -= 1

def pop_list(lis, times):
    while times > 0:
        lis.pop()
        times -= 1


sol = Solution()
sol.combinationSum([1,2],4)
