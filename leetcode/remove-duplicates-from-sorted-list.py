# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        point1 = head
        temp = head.next
        point1.next = None
        point2 = temp
        rhead = point1
        if not point2:
            return rhead
        while point2:
            if point1.val == point2.val:
                point2 = point2.next
            else:
                temp = point2.next
                point1.next = point2
                point1 = point2
                point1.next = None
                point2 = temp
        return rhead
        
