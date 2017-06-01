#!/usr/bin/python

#value_list = [1,[2],5]
value_list = [1,[2],[[4,[1]],4],5]
#######
def depth_sum(value_list):
    """ Value list depth sum """
    return get_all_sum(value_list, 0)
 

def get_all_sum(ele, level): 
    sum = 0
    if type(ele) == list:  # 1, [2,3]
        for i in ele:
            sum += get_all_sum(i, level+1)
        return sum
    else:
        return ele*level
###########



def reverse_depth_sum(value_list):
    """ Value list depth sum - reverse value """
    height = find_depth(value_list)
    print "got height %s"%height
    return get_all_sum_rev(value_list, height)


def find_depth(value):
    max_depth = 0
    if type(value) == list:
        for i in value:
            tempheight = find_depth(i)
            if tempheight > max_depth:
                max_depth = tempheight
        return max_depth + 1
    else:
        return 1 
   
def get_all_sum_rev(ele, level):
    sum = 0 
    if type(ele) == list:
        for i in ele:
            sum += get_all_sum_rev(i, level-1)
        return sum 
    else:
        print "%s %s"%(ele, level)
        return ele*level


input = [[1,2], 1, [2, [2,1]]]
print reverse_depth_sum(input)
