#!/usr/bin/python

stats = [(1981,1999), (1943,1949), (1911,1930),(1901,1950),(1910,1945),(1947,1989), (1989,2000)]

miny=1900
maxy=2000

def get_population_array(stats):
    population_increase = [ 0 for i in range(maxy-miny+2)]
    for i in stats:
        byear = i[0]-miny
        dyear = i[1]-miny
        population_increase[byear] += 1
        population_increase[dyear+1] -= 1
    return population_increase    


def get_max_alive(population_increase):
    max_alive = 0
    max_alive_year = 0
    running_alive = 0
    for i in range(len(population_increase)):
        running_alive += population_increase[i] 
        if running_alive > max_alive:
            max_alive = running_alive
            max_alive_year = miny+i
    print max_alive, max_alive_year

parray = get_population_array(stats)
print parray
get_max_alive(parray)
