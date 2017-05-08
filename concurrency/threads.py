#!/usr/bin/python

import time
import threading


class MyThread(threading.Thread):
    """ Multithread subject class """     
    def __init__(self, id, func):
        super(MyThread, self).__init__()
        self.id = id 
        self.func_exe = func

    def run(self):
        print "Starting thread %s"%self.id
        self.func_exe.__call__()
        print "Exiting thread %s"%self.id

def first():
    print "Executing first "
    threadlock1.release()

def second():
    threadlock1.acquire()
    print "Executing second"
    time.sleep(5) 
    threadlock2.release()

def third():
    threadlock2.acquire()
    print "Executing third"
    threadlock2.release()
    threadlock1.release()

t1 = MyThread(1, first)
t2 = MyThread(2, second)
t3 = MyThread(2, third)

threadlock1 = threading.Lock() 
threadlock2 = threading.Lock() 
threadlock3 = threading.Lock() 
threadlock1.acquire()
threadlock2.acquire()
threadlock3.acquire()
t1.start()
t2.start()
t3.start()
print "Exiting main program"
