#!/usr//bin/python

import Queue
import threading
import time

class BlockingQueue(object):
    def __init__(self, maximum):
        self.queue = Queue.Queue()
        self.maxlen = maximum

    def addItem(self, item):
        Condition.acquire()
        if self.queue.qsize() > self.maxlen:  # if size is smaller
            Condition.wait()
        self.queue.put(item)
        Condition.notifyAll()
        Condition.release()
             
    def getItem(self):
        Condition.acquire()
        if self.queue.qsize() == 0:
            Condition.wait()
            print "EMPTY QUEUE" 
        temp = self.queue.get()
        Condition.notifyAll()
        Condition.release()
        return temp 
            

Condition = threading.Condition()   ## Condition - for empty
bq = BlockingQueue(3) 

def worker(n):
    while True:
        bq.addItem(n)
        time.sleep(1) 
        if n == 4:
            item = bq.getItem()
            print item
  
for i in range(10):
    t = threading.Thread(target=worker,args=(i,))
    t.start()

