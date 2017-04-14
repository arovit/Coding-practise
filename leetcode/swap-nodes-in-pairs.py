# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        pnode = None
        newhead = None
        while (a and a.next):
            #print a.val
            if pnode:
                pnode.next = a.next
            b = a.next.next
            a.next.next = a
            if not newhead:
                newhead = a.next
            a.next = b
            pnode = a
            a = b
        if not newhead:
            return head
        else:
            return newhead
