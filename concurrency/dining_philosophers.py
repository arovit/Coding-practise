#!/usr/bin/python

import time
import threading

class chopStick(object):
    def __init__(self, id):
        self.lock = threading.Lock()
        self.id = id
    def _pickUp(self):
        self.lock.acquire()
    def _putDown(self):
        self.lock.release()
  
class Philosopher(threading.Thread):
    def __init__(self, id, left_chop, right_chop):
        self.id = id
        if left_chop.id > right_chop.id: ## Left should be smaller
            left_chop, right_chop = right_chop, left_chop
        self.leftc =left_chop
        self.rightc =right_chop
        super(Philosopher, self).__init__()

    def pickUp(self):
        print "Philosopher %s picking up left fork"%self.id
        self.leftc._pickUp()
        print "Philosopher %s picking up right fork"%self.id
        self.rightc._pickUp()

    def putDown(self):
        self.leftc._putDown()
        self.rightc._putDown()
        print "Philosopher %s has put both fork down"%self.id

    def chew_and_think(self):
        time.sleep(2)

    def eat(self):
        print "Philosopher %s ready to eat"%self.id
        self.pickUp()
        self.chew_and_think()
        self.putDown()
        print "Philosopher %s done with eating"%self.id

    def run(self):
        for i in range(5):
            self.eat()


c1 = chopStick(1)
c2 = chopStick(2)
c3 = chopStick(3)

p1 = Philosopher(1, c2, c1)
p2 = Philosopher(2, c3, c2)
p3 = Philosopher(3, c1, c3)

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()
