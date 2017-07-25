#!/usr/bin/python

import threading
import random
import time


class BoundedBlockingQueue(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.cvar = threading.Condition()
        self.data_queue = None
    
    def init(self, capacity):
        self.lock.acquire()
        if self.data_queue is None:
            self.data_queue = []
            self.capacity = capacity
        else:
            raise Exception # already initialized 
        self.lock.release()

    def push(self, ele): # push into data_queue
        self.cvar.acquire()
        if len(self.data_queue) == self.capacity: # queue is full
            self.cvar.wait()
        self.data_queue.append(ele)
        self.cvar.notify()
        self.cvar.release()
        
    def pop(self):  # pop from data_queue 
        self.cvar.acquire()
        if len(self.data_queue) == 0:
            self.cvar.wait()
        ele = self.data_queue.pop()
        self.cvar.notify()
        self.cvar.release()
        return ele
        

queue = BoundedBlockingQueue()
queue.init(10)

class ProducerThread(threading.Thread):
    def run(self):
        nums = range(3)
        global queue
        while True:
            num = random.choice(nums)
            queue.push(num)
            print "Produced", num
            time.sleep(random.randint(1,3))


class ConsumerThread(threading.Thread):
    def run(self):
        nums = range(3)
        global queue
        while True:
            num = random.choice(nums)
            num = queue.pop()
            print "Consumed", num
            time.sleep(random.randint(1,4))

ProducerThread().start()
ConsumerThread().start()
