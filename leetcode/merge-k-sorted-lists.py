#!/usr/bin/python

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        for i in range(0, len(lists)-1):
            head = self.merge2List(lists[i], lists[i+1])
            print head
            node = head
            while node:
                print node.val
                node = node.next 
            lists[i+1] = head
        return lists[-1]

    def merge2List(self, node1, node2):
        head1 = node1
        prev = None
        while node1 and node2:
            if node1.val >= node2.val:
                if prev:
                    prev.next = node2
                else:
                    head1 = node2
                temp = node2.next
                node2.next = node1
                prev = node2
                node2 = temp
            else:
                prev = node1
                node1 = node1.next
        if node2:
            prev.next = node2
        return head1   
        

head1 = ListNode(1)
head1.next = ListNode(10)

head2 = ListNode(2)
head2.next = ListNode(7)
head2.next.next = ListNode(14)

head3 = ListNode(3)
head3.next= ListNode(5)
head3.next.next = ListNode(9)
head3.next.next.next = ListNode(14)
head3.next.next.next.next = ListNode(18)
head3.next.next.next.next.next = ListNode(29)


sol = Solution()
node = sol.mergeKLists([head1, head2, head3])

