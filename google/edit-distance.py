#!/usr/bin/python


def edit_distance(str1, str2, len1, len2, hash_map):
    key = "%s|%s"%(len1,len2)
    if hash_map.has_key(key):
        return hash_map[key] 
    if len1 == 0: 
        hash_map[key] = len2
        return len2 # insert
    if len2 == 0:
        hash_map[key] = len1
        return len1 # remobe
    if str1[len1-1] == str2[len2-1]:
        hash_map[key] =  edit_distance(str1, str2, len1-1, len2-1, hash_map)
        return hash_map[key]
    else:
        hash_map[key] = 1 + min( edit_distance(str1, str2, len1, len2-1, hash_map), 
			         edit_distance(str1, str2, len1-1, len2, hash_map), 
			         edit_distance(str1, str2, len1-1, len2-1, hash_map )) 
        return hash_map[key] 




print edit_distance("arovi", "aro", 5, 3, {}) 

def edit_distance_dp(str1, str2, len1, len2 
    dp_matrix = [[0 for i in range(len2)] for j in range(len1)]  
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0:
                dp_matrix[i][j] = dp_matrix[j]   # insert min operation 0-1 - 1, 0-2 -2, 0-4 - 4 ... etc
            if j == 0:
                dp_matrix[i][j] = dp_matrix[i]   # remove min operation 1-0 - 1, 2-0 -2, 4-0 - 4 ... etc
            elif str1[len1] == str2[len2]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1]   
            else:
                dp_matrix[i][j] = 1 + min(dp_matrix[i-1][j], dp_matrix[i][j-1], dp_matrix[i-1][j-1])
    return dp_matrix[len1][len2]                
    

