#!/usr/bin/python

N = 2
#matrix question - island n*n, man takes 1 step 
def get_probability(x,y,n,hash_map):
    if n==0:
        return 1.0      
    key= "%s|%s|%s"%(x,y,n)
    if key in hash_map:
        return hash_map[key]
    p = 0.0
    if y > 0:
        p += 0.25 *get_probability(x, y-1, n-1, hash_map)
    if y < N-1:
        p += 0.25 * get_probability(x, y+1, n-1, hash_map)
    if x > 0:
        p += 0.25 * get_probability(x-1, y, n-1, hash_map)
    if x < N-1:   
        p += 0.25 * get_probability(x+1, y, n-1, hash_map)
    
    hash_map[key] = p
    return p


print get_probability(0,0,1,{})
