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
        self.length = 0
        self.curNode = self.head
        self.odd = 0
        self.even = 0
    
    def insertNode(self, data):
        node = Node()
        node.data = data
        node.next = None
        if self.head.data == None:
            self.head = node
            self.curNode = node
        else:
            self.curNode.next = node
            self.curNode = node 
        self.length += 1
        
    def checkPalindrome(self):
        self.middle = self.length/2 -1 
        if self.length%2 == 1:
            self.odd = 1
        else:
            self.even = 1
        if self.checkMiddle(self.head, 0):
            print "Its a Palindrome"
        else:
            print "It's not a palindrome"

    @staticmethod
    def compareNode(node1, node2):
        if node1.data == node2.data:
            if node2.next:
                return node2.next
            else:
                return True
        else:
            return None

    def checkMiddle(self, node, count):
        temp = node
        if count < self.middle:
            right = self.checkMiddle(node.next, count+1)
            if temp and right and (temp.data == right.data):
                if count == 0:
                    return True
                else:
                    return right.next
            else:
                return None 
        elif count == self.middle:
            if self.odd:
                return LinkedList.compareNode(node, node.next.next)
            else:
                return LinkedList.compareNode(node, node.next)
        
l = LinkedList()
l.insertNode(1)
l.insertNode(2)
l.insertNode(1)
l.checkPalindrome()
