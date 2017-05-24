#!/usr/bin/python


class Ball(object):
    def __init__(self, x, v):
        self.x = x  # x co-ordinate
        self.v = v  # velocity



TLENGTH = 10

def findTimeCleanTable(list_of_balls):
    ## find min time to collide
    sorted(list_of_balls, key=lambda x:x.x)
    printPositions(list_of_balls) 
    mctime, mcindex = firstTimeOfCollision(list_of_balls)
    print mctime, mcindex
    if mctime != 9999: 
        findNewPositions(list_of_balls, mctime, mcindex)
        return findTimeCleanTable(list_of_balls)
    else:  ## no collision happening
        # find last ball - both could be moving in opposite direction 
        maxtime = 0
        for i in list_of_balls:
            if i.v > 0:
                time = (TLENGTH - i.x)/i.v
            else:  
                time = -1*(i.x)/i.v
            if time > maxtime:
                maxtime = time 
        return maxtime      


def findNewPositions(list_of_balls, mctime, mcindex):
    to_be_removed_indexes = []
    for bindex in range(0, len(list_of_balls)):
        dist = list_of_balls[bindex].v * mctime 
        list_of_balls[bindex].x = list_of_balls[bindex].x + dist        
        if bindex in mcindex:
            list_of_balls[bindex].v = -1 *list_of_balls[bindex].v
        if (list_of_balls[bindex].x > TLENGTH) or (list_of_balls[bindex].x < 0):
            to_be_removed_indexes.append(bindex) 
    for i in to_be_removed_indexes:
        del list_of_balls[i]     

def firstTimeOfCollision(list_of_balls):
    min_time_to_collision = 9999
    collide_indexes = (0,0)
    for bindex in range(0, len(list_of_balls)-1):
        if (list_of_balls[bindex].v < 0) and (list_of_balls[bindex+1].v > 0):  ##  Only negative - positive will collide - negative - left, positive - right 
            time = abs((list_of_balls[bindex].x - list_of_balls[bindex+1].x)/(2*list_of_balls[bindex+1].v))
            print time
            if time < min_time_to_collision:
                min_time_to_collision = time
                collide_indexes = (bindex,bindex+1) 
    return min_time_to_collision, collide_indexes

def printPositions(list_of_balls):
    for i in list_of_balls:
        print "%s,  %s"%(i.x, i.v)

list_of_balls = []
list_of_balls.append(Ball(4,-1))
list_of_balls.append(Ball(2,1))
print findTimeCleanTable(list_of_balls)
