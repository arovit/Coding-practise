#!/usr/bin/python


class Node:
    def __init__(self):
        self.data = None
        self.next = None
    def __str__(self):
        return "Data %s: Next -> %s"%(self.data, self.next) 


class LinkedList:
    def __init__(self):
        self.head = Node() 
        self.curNode = self.head
    
    def insertData(self, data):
        node = Node()
        node.data = data
        node.next = None
        if self.head.data == None:
            self.head = node
            self.curNode = node
        else:
            self.curNode.next = node
            self.curNode = node 
        return node

    def insertNode(self, node):
        self.curNode.next = node
        self.curNode = node
    
    def printList(self):
        print self.head

    def loopDetect(self):
        """ FLoyd's loop detection algo - O(N) """
        slower = self.head
        if slower.next and slower.next.next: 
            faster = slower.next.next
        else:
            return False
 
        while True:
            if slower == faster:
                return True 
            if faster.next and faster.next.next:
                faster = faster.next.next 
            else:
                return False 
            if slower.next:
                slower = slower.next 
            else:
                return False

l = LinkedList()
l.insertData(1)
nod = l.insertData(2)
l.insertData(34)
l.insertData(4)
l.insertData(5)
l.insertData(6)
#l.insertNode(nod)
if l.loopDetect():
    print "Loop detected"
else:
    print "Loop not detected"
