#!/usr/bin/python

# Write the weaving logic
# 1, 2
# 3, 4
# 1,2,3,4 or 1,3,2,4 or 1,3,4,2 or 3,4,1,2 or 3,1,4,2 or 3,1,2,4
# 1,2 
# 3


def weavingLogic(list1, list2, prefix):
    if list1: 
        ele = list1[0]
	prefix.append(ele)
        weavingLogic(list1[1:], list2, prefix)
        prefix.pop()
    if list2:
        ele = list2[0]
	prefix.append(ele)
        weavingLogic(list1, list2[1:], prefix) 
        prefix.pop()
    if not list1 and not list2:
        print prefix


weavingLogic([1,2],[3,4], [])
