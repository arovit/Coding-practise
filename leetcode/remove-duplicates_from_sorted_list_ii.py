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
        hash_of_repeated_numbers = self.get_all_repeated_nodes(head)
        newhead = None
        newnode = None
        temp = head
        print hash_of_repeated_numbers
        while temp:
            jumpnode = temp.next
            if temp.val not in hash_of_repeated_numbers:
                if not newnode:
                    newnode = temp
                    newnode.next = None
                    newhead = newnode
                else:
                    newnode.next = temp
                    newnode = temp
                    newnode.next = None
            temp = jumpnode
        return newhead
    
    def get_all_repeated_nodes(self, head):
        temp = head
        repeatNumbers = {}
        while temp and temp.next:
            if temp.val == temp.next.val:
                repeatNumbers[temp.val] = 1
            temp = temp.next
        return repeatNumbers
