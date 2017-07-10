#!/usr/bin/python

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.mainStack = [(0,nestedList)]
        
    def next(self):
        """
        :rtype: int
        """
        curIndex, curList = self.mainStack[-1]
        ele = curList[curIndex]
        curIndex += 1
        self.mainStack[-1] = (curIndex, curList)
        return ele

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.mainStack:
            return False
        curIndex, curList = self.mainStack[-1]
        if curIndex >= len(curList):  # curList is finished
            self.mainStack.pop()
            return self.hasNext()
        if curList[curIndex].getInteger() == None:
            self.mainStack[-1] = (curIndex+1, curList)
            self.mainStack.append((0,curList[curIndex].getList()))
            return self.hasNext()
        if curIndex < len(curList):
            return True
        return False
