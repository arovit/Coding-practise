#!/usr/bin/python

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = []
        if len(lists) == 0:
            return []
        elif len(lists) == 1:
            return lists[0]
        for i in lists:
            head = self.merge2lists(i, head)
        return head    
        
    def merge2lists(self, head1, head2):
        node1 = head1
        node2 = head2
        newhead = head1
        prev = None
        while node1 and node2:
            #print node1.val, node2.val
            if node2.val < node1.val:   # if node2 is less than node1
                temp = node2.next       # note the next of node2
                node2.next = node1      # make node2 point to node1
                if prev:                # if prev, then modify prev to point to node2
                    prev.next = node2   
                else:                   # else if no prev, make node2 as head
                    newhead = node2
                prev = node2            # make node2 as prev
                node2 = temp
            elif node1.val <= node2.val: # if node1 is less than node2
                prev = node1
                node1 = node1.next
    
        if (not node1) and node2:
            if prev:
                prev.next = node2
            else:
                newhead = node2
        return newhead    
            

