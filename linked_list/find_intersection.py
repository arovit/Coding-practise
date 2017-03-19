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
        return self.curNode 
    
    def addNode(self, node):
        self.curNode.next = node
        self.curNode = node
   
    def getLength(self):
        count = 0
        llist = self.head
        while llist:
            count += 1 
            llist = llist.next 
        return count
     
    @staticmethod
    def getIntersect(list1, list2):
        """ Get the intersecting node of two linked lists """
        node1 = list1.head
        node2 = list2.head
        len1 = list1.getLength() 
        len2 = list2.getLength() 
        if len1 > len2:
            while len1 > len2:
               node1 = node1.next
               len1 = len1 - 1
        elif len2 > len1:
            while len2 > len1:
               node2 = node2.next 
               len2 = len2 -1 
        else: 
            pass # We are good
        while node1 and node2:
            if node1 == node2: 
               return node1
            else:
               node1 = node1.next
               node2 = node2.next

    def printList(self):
        print self.head


l1 = LinkedList()
l1.insertData(1)
l1.insertData(9)
l1.insertData(8)
l1.insertData(2)
l1.insertData(111)
l1.insertData(24)
l1.insertData(12)
intern = l1.insertData(3)
l1.insertData(4)
l1.insertData(2)

l2 = LinkedList()
l2.insertData(1)
l2.insertData(12)
l2.insertData(2)
l2.insertData(8)
l2.insertData(19)
l2.addNode(intern)

l1.printList()
l2.printList()   

intersect = LinkedList.getIntersect(l1, l2)
if intersect:
    print "Intersecting at %s"%intersect.data
else:
    print "Neither intersecting nor interesting"

 
