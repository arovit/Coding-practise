#!/usr/bin/python

# Find line intersection of two points

# p1 (x1, y1)
# p2 (x2, y2)

# p3 (x3, y3)
# p4 (x4, y4)


def line_equation(p1, p2):
   """ Line equation of then form Ax + By = C
   A = y2 - y1
   B = x1 - x2
   C = Ax1 + By1
   AX + BY = C
   """ 
   A = p2[1] - p1[1]
   B = p1[0] - p2[0]
   C = A*p1[0] + B*p2[0]
   return (A,B,C)
    



def intersect(tuple1, tuple2):
    """ A1, B1, C1, A2, B2, C2"""
    diff = tuple1[0]*tuple2[1] - tuple2[0]*tuple1[1]    
    if diff == 0:
        # Lines are parallel
        return None, None
    else:
        # B2C1 - B1C2 /diff
        x = float((tuple2[1]*tuple1[2] - tuple1[1]*tuple2[2])/diff)
        # C2A1 - C1A2/ diff 
        y = float((tuple2[2]*tuple1[0] - tuple1[2]*tuple2[0])/diff) 
        return x,y


point1 = (2,10)
point2 = (1,7)

point3 = (1,8)
point4 = (2,6)

eq1 = line_equation(point1, point2)
eq2 = line_equation(point3, point4)

print intersect(eq1, eq2)
