#!/usr/bin/python

import time
import threading

class chopStick(object):
    def __init__(self):
        self.lock = Threading.Lock()
    def _pickUp(self):
        self.lock.acquire()
    def _putDown(self):
        self.lock.release()
  
class ThinkEat(threading.Thread):
    def __init__(self, left_chop, right_chop):
        self.leftc =left_chop
        self.rightc =right_chop
    def pickUp(self):
        self.leftc._pickUp()
        self.rightc._pickUp()
    def putDown(self):
        self.leftc._putDown()
        self.rightc._putDown()
    def chew_and_think(self):
        time.sleep(1)
    def eat(self):
        self.pickUp()
        self.chew_and_think()
        self.putDown()


