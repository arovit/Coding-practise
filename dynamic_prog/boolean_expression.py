#!/usr/bin/python

# input : boolen exp , has operator every next char 1&0|1&1^1
# output: number of ways target bool value can be achieved 



def get_n_ways(expression, target):
    if len(expression) == 1:
        if expression[0] == '1' and target == True:
        	return 1 
        elif expression[0] == '0' and target == False:
        	return 1 
        else:
            return 0 
    ways = 0
    for i in range(1,len(expression),2):
        left_True = get_n_ways(expression[:i], True)
        left_False = get_n_ways(expression[:i], False)
        right_True = get_n_ways(expression[i+1:], True)
        right_False = get_n_ways(expression[i+1:], False)
        print "Exp: %s left_True: %s, left_False: %s, right_True: %s, right_False: %s"%(expression, left_True, left_False, right_True, right_False)
        if expression[i] == '&':
            if target == True:
                ways += (left_True * right_True) 
            if target == False:
                ways += (left_True * right_False  + left_False * right_True + left_False * right_False)
        if expression[i] == '|':
            if target == True:
                ways += (left_True * right_False  + left_False * right_True + left_True * right_True)
            if target == False:
                ways += (left_False * right_False)
        if expression[i] == '^':
            if target == True:
                ways += (left_True * right_False  + left_False * right_True)
            if target == False:
                ways += (left_False * right_False + left_True * right_True)
    return ways   

print get_n_ways('1|1|0&1^1|0',True) 
