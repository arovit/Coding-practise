#!/usr/bin/python

class Node(object):
    """ LL node """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None 


class LRU(object):
    """ Using doubly linked list """

    def __init__(self):
        self.listHead = None 
        self.cache = {}  # cache key - > node
   
    def getValue(self, key):
        if key not in self.cache:
            return None
        else:
            node = self.cache(key)
            self.moveToHead(node)
            return node.data

    def moveTohead(self, node):
        if node == self.listHead: # if already head
            return 
        if node.next == None:     # if was tail
            node.prev.next = None # mark prev as tail
            node.prev = None      # makr prev as None
            node.next = self.listHead # mark next as head 
            self.listHead.prev = node  # MArk prev of headnode 
            self.listHead = node  
        else: 
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = self.listHead
            self.listHead.prev = node
            self.listHead = node
         
    def insertKey(self, key):
        node = Node(key)
        self.cache.update({key:node})
        self.addNodeToList(node):

    def addNodeToList(self, node):
        if self.listHead is None:
            self.listHead = node
        else:
            self.listHead.prev = node  ## 
            node.next = self.listHead
            self.listHead = node
        
