#!/usr/bin/python

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        j=len(nums)-1 
        if len(nums) == 1:
            if nums[0] != val:
                return 1
            else:
                return 0
        while i <= j:
            if nums[i] != val:
                i = i + 1
            else:
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i = i + 1
                else:
                    j = j -1
        if i<0: 
            i = 0
        return i 
 
def test_input(solver,inp1,inp2,result):
    ans = solver(inp1,inp2) 
    if ans == result:
        print "OK"
    else:
        print "Failed for inp %s %s: Result %s, Expected %s"%(inp1, inp2, ans, result) 

sol = Solution()
sol = sol.removeElement
test_input(sol,[4,4],5,2) 
test_input(sol,[],5,0) 
test_input(sol,[5],5,0) 
test_input(sol,[5,5,5],5,0) 
test_input(sol,[4,5,5],5,1) 
test_input(sol,[4,5],5,1) 
test_input(sol, [4,4,5],5,2) 
