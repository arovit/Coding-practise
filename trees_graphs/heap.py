#!/usr/bin/python

from trees import Node

class HeapTree(object):
    def __init__(self):
        self.array = []   ## the data is stored in an array. Because easy to access across nodes since it has to be complete tree

    def initData(self, data):
        self.array.extend(data)
          
    def heapifyDown(self, parent_index):
        """ This is min heapify. Trickle down """
        lchild = 2*parent_index + 1
        rchild = lchild + 1    
        min_vale = parent_index
        if lchild < len(self.array) and (self.array[lchild] < self.array[min_vale]):
            min_vale = lchild
        if rchild < len(self.array) and (self.array[rchild] < self.array[min_vale]): 
            min_vale = rchild 
        if min_vale != parent_index:
            self.array[min_vale], self.array[parent_index] = self.array[parent_index], self.array[min_vale]
            self.heapifyDown(min_vale)
 
    def heapifyUp(self, pindex):
        lchild = 2*pindex + 1
        rchild = lchild + 1    
        print "%s %s %s"%(lchild, rchild, pindex)
        min_vale = pindex
        if lchild < len(self.array) and (self.array[lchild] < self.array[min_vale]):
            min_vale = lchild
        if rchild < len(self.array) and (self.array[rchild] < self.array[min_vale]): 
            min_vale = rchild 
        if min_vale != pindex :
            self.array[min_vale], self.array[pindex] = self.array[pindex], self.array[min_vale]
            if pindex != 0:
                self.heapifyUp((pindex-1)/2)

    def insertData(self, data):
        self.array.append(data)
        pindex = (len(self.array)-1)/2
        self.heapifyUp(pindex)

    def build_heap_tree(self):
        for i in range(len(self.array)/2, -1, -1):
            self.heapifyDown(i) 
 
    def printf(self):
        print self.array 



ht = HeapTree()
ht.initData([42, 24, 29, 40, 38, 86, 72]) 
ht.printf()
ht.build_heap_tree()
ht.printf()
data = raw_input("ENter data to insert\n")
ht.insertData(int(data))
ht.printf()
