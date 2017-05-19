#!/usr/bin/python

# Print all subsets of a given set

#[1,2] = [1][2][1,2][]

def get_all_subsets(slist):
    if len(slist) == 1:
        return [slist[0],'']
    previos_set = get_all_subsets(slist[1:])
    new_set = []
    for i in previos_set:
        new_set.append(i+slist[0])
    previos_set.extend(new_set)
    return previos_set

print get_all_subsets('123')

