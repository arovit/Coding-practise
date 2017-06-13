# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        headPointer = head
        slowPointer = head
        fastPointer = head
        fastPointer = self.formInitialGap(fastPointer, k)
        slowPointer, fastPointer = self.incrementBothTilEnd(slowPointer, fastPointer)
        self.doTheRotation(headPointer, slowPointer, fastPointer)
    
    def formInitialGap(self, fastPointer, gap):
        for i in range(gap):
            fastPointer = fastPointer.next
        return fastPointer
    
    def incrementBothTilEnd(self, slow, fast):
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        return slow, fast
        
        
    def doTheRotation(head, slow, fast):
        fast.next = head
        newhead = slow.next
        slow.next = None
        return newhead
