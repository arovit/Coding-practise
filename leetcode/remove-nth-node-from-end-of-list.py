#!/usr/bin/python

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        returnnode = head # to return
        frwdnode = head
        prev = head
        n = n -1
        while n:
            if not frwdnode.next:  ## the given list if shorter
                break       ## return same head node
            frwdnode = frwdnode.next
            n -= 1
        if n:  ## we could not go 3 nodes forward
            return head
        ## frwdnode is now 'n' steps forward
        while True:
            if not frwdnode.next:
                break  # head is pointing to last nth node
            else:
                frwdnode = frwdnode.next
                prev = head
                head = head.next
        ## Now delete the node pointed by head
        print head.val
        print frwdnode.val
        print prev.val
        if head.next:
            head.val = head.next.val
            head.next = head.next.next
            return returnnode
        else:
            if prev != head:
                prev.next = None
                return returnnode
            else:
                return []










