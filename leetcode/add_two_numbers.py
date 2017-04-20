# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        remain = 0
        count = 0
        head = None
        temp = None
        while True:
            if l1 == None and l2 == None:
                if remain:
                    node = ListNode(remain)
                    temp.next = node
                break
            a = b = 0
            if l1:
                a = l1.val
            if l2:
                b = l2.val  
            res = a + b + remain
            store = res % 10     
            remain = res / 10
            node = ListNode(store)
            if not head:
                head = node
            if temp:
                temp.next = node
            temp = node 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head     
            
