#!/usr/bin/python


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resultlist = []
        self.checksum(0, candidates, target, [])
        self.cache = {}
            
    def checksum(self, index, candidates, target, lastarray):
        if target < 0:
            return 
        elif target == 0:
            newlist = lastarray[:] 
            newlist.sort() 
            if newlist not in self.resultlist:
                self.resultlist.append(newlist)
            return
        for i in range(index, len(candidates)):
            remain = target - candidates[i]
            lastarray.append(candidates[i])
            self.checksum(i+1, candidates, remain, lastarray)
            lastarray.pop()



sol = Solution()
candi = [10, 1, 2, 7, 6, 1, 5]
sol.combinationSum2(candi, 8)
print sol.resultlist
