#!/usr/bin/python

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
     def __str__(self):
         return "%s -> %s"%(self.val, self.next)   

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        prev = None 
        node = head  
        while count < m:
            prev = node 
            node = node.next
            count += 1
        # Node is at m
        start = node
        node1 = node
        node2 = node1.next 
        if prev: print "prev at %s"%prev.val
        print "start at %s"%start.val
        while count < n:   
           # print "node1 %s"%node1.val
            temp = node2.next    
            node2.next = node1   
            node1 = node2
            node2 = temp
            count += 1
        #print "node1 %s"%node1.val
        #print "node2 %s"%node2.val
        if prev:
            prev.next = node1  
        else:
            head = node1 
        start.next = node2
        print head
         


sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print head
sol.reverseBetween(head, 1, 1)
#print head
