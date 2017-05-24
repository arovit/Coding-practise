#!/usr/bin/python



def find_small_diff(a,b):
   a = sorted(a)
   b = sorted(b)
   i = j = 0
   min = 999999999999999999 
   min_a = 0
   min_b = 0
   while (i  < len(a)) and (j < len(b)):
       if abs(a[i]-b[j]) < min:
           min = abs(a[i]-b[j])
           min_a = a[i]
           min_b = b[j]
       if (a[i] < b[j]):
           i += 1
       elif (a[i] > b[j]):
           j += 1
   print min_a, min_b

l1 = [1,3,15,11,2]
l2 = [23,127,235,19,8] 
find_small_diff(l1, l2)
