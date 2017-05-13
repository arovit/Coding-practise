#!/usr/bin/python


pots = [1,2,3,4,5,19,19,2,3,4,18]


def max_gold(pot,start,end):
   if start > end:
       return 0  
   select_start = pots[start] + min(max_gold(pots, start+2, end), max_gold(pots, start+1, end-1))  
   select_last = pots[end] + min(max_gold(pots, start+1, end-1), max_gold(pots, start, end-2))  
   return max(select_start, select_last)


print max_gold(pots, 0, len(pots)-1)
