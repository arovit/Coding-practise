#!/usr/bin/python

class Solution(object):
    def printList(self, ln):
        while ln:
            print ln.val 
            ln = ln.next
            
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prevl1 = None
        if l1:
            head = l1
        else:
            head = l2
        while l1 and l2:
            #print l1.val, l2.val
            if l1.val >= l2.val:
                if prevl1:
                    prevl1.next = l2
                else:
                    head = l2
                prevl1 = l2
                temp = l2.next
                l2.next = l1
                l2 = temp
            else:
                prevl1 = l1
                l1 = l1.next
        print "L1",self.printList(l1)
        print "L2",self.printList(l2)
        print "head",self.printList(head)
        if l2:
            if prevl1: prevl1.next = l2
        return head
            
