#!/usr/bin/python


class Box(object):
    def __init__(self, h, w, b):
        self.h = h
        self.w = w
        self.b = b 



def cal_max_height(sort_boxes, base, height):
    max_height = height 
    for index, i in enumerate(sort_boxes):
        if (height == 0) or (i.h < base.h and i.w < base.w and i.b < base.b):
            h = cal_max_height(sort_boxes[index+1:], i, height+i.h)
            print h 
            if h > max_height:
                max_height = h 
    return max_height


b1 = Box(3,4,5)
b2 = Box(2,3,3)
b3 = Box(4,3,1)
b4 = Box(6,7,8)
b5 = Box(3,4,3)
b6 = Box(1,2,2)
b7 = Box(1,1,1)
blist = [b4,b1,b2,b3,b4,b5,b6,b7]
bslist = sorted(blist, key=lambda x:x.h)[::-1]
print cal_max_height(bslist, None, 0)
