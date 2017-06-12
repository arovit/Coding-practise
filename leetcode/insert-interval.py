#!/usr/bin/python


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "%s, %s"%(self.start, self.end)

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        findex = self.findPosition(intervals, newInterval)
        intervals.insert(findex, newInterval)
        start = 0 if findex == 0 else findex-1
        return self.mergeFromIndex(start, intervals, newInterval)
        
    def mergeFromIndex(self, index, intervals, insertedInterval):
        if index == len(intervals)-1:
            return intervals
        resultant = intervals[:index]
        resultant.append(intervals[index])
        index += 1
        while index < len(intervals):
            nInterval = intervals[index]
            rInterval = resultant.pop()
            print "index %s Ninterval %s %s"%(index, nInterval.start, nInterval.end)
            print "index %s Rinterval %s %s"%(index, rInterval.start, rInterval.end)
            if nInterval.start > rInterval.end:  # disjoint interval
                resultant.append(rInterval)
                if ( nInterval != insertedInterval) or index == len(intervals)-1:
                    break
                else:
                    resultant.append(nInterval)
            elif nInterval.start == rInterval.end:
                rInterval.end = nInterval.end
                resultant.append(rInterval)
            else:
                resultant.append(self.mergeTwoIntervals(rInterval, nInterval))
            index += 1
        print "index %s"%index
        print intervals[index:]
        resultant.extend(intervals[index:])
        return resultant
    
    
    def mergeTwoIntervals(self, int1, int2):
        if int1.end >= int2.end:
            return int1
        elif int1.end < int2.end:
            int1.end = int2.end
            return int1
        
        
    def findPosition(self, intervals, newInterval):
        foundIndex = len(intervals)
        for index, val in enumerate(intervals):
            if newInterval.start < val.start:
                foundIndex = index
                break
        return foundIndex
 

