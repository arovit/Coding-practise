#!/usr/bin/python


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smallhead = bighead = spoint = bpoint = None
        temp = head
        while temp:
            ntemp = temp.next
            temp.next = None
            if temp.val >= x:
                if bpoint:
                    bpoint.next = temp
                    bpoint = temp
                else:
                    bighead = temp
                    bpoint = temp
            else:
                if spoint:
                    spoint.next = temp
                    spoint = temp
                else:
                    smallhead = temp
                    spoint = temp
            temp = ntemp
        if spoint:
            spoint.next = bighead
            return smallhead
        else:
            return bighead
    


