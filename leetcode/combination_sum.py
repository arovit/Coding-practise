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
    
    def checksum(self, listn, tsum, index, ways, tresult):
        print tresult, tsum
        if tsum == 0:
            self.resultlist.append(tresult[:])
            return 1
        elif tsum < 0:
            return 0
        for i in range(index, len(listn)):
            num = listn[i]
            while num <= tsum:
                tresult.append(num)
                if self.checksum(listn, tsum-num, index+1, ways, tresult):
                    ways += 1
                tresult.pop()
                num = num << 1
        return ways


sol = Solution()
sol.combinationSum([2, 3,6,7],7)
