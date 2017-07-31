#!/usr/bin/python


# 123, 132, 231, 213, 312, 321

def gen_permutation(prefix, ostr):
    if ostr == '':
        print prefix
    for i in range(len(ostr)):
        gen_permutation(ostr[i]+prefix, ostr[:i]+ostr[i+1:])
                    

gen_permutation('','123')

# [1,2,3,4,5]
def gen_combination(items, n):
    result = []
    if n == 1:
        for i in range(len(items)):
            result.append([items[i]])
        return result
    elif len(items) == n:
        result.append(items)
        return result
    else:
        tmp1 = gen_combination(items[1:],n)
        tmp2 = gen_combination(items[1:],n-1)
        for j in tmp2:
            j.append(items[0]) 
        result.extend(tmp1)
        result.extend(tmp2)
        return result


print gen_combination([1,2,3],2)


1. Consistent hashing- Ring like structure , hosts are allocated in between values
2. CAP Theorem - Consistency / Availability/ Partition 
3. Load Balancing
4. Caching - LRU, LFU, CDN, Global , Distributed 
5. Horizontal / Vertial partitioning 
6. Horizontal partition - list, rr, key, composite
7. Indexes, Proxies
8. Redundancy


