#!/usr/bin/python


def distinct_paths(h, w, badpaths):
    bad_paths = {}
    for i in badpaths:
        x1, y1, x2, y2 = map(int, i.split(' '))
        bad_paths[(x1,y1,x2,y2)] = 1
        bad_paths[(x2,y2,x1,y1)] = 1
    dp_paths = [[ 0 for i in range(w+1)] for j in range(h+1)]     
    dp_paths[0][0] = 1 
    for i in range(h+1):
        print dp_paths
        for j in range(w+1):
            if (i==0 and j==0):
                continue  
            if (i,j,i,j-1) not in bad_paths and (j-1 >= 0):
                dp_paths[i][j] = dp_paths[i][j-1] + dp_paths[i][j]        
            if (i-1,j,i,j) not in bad_paths and (i-1 >= 0):
                dp_paths[i][j] = dp_paths[i-1][j] + dp_paths[i][j]        
    print dp_paths
    return dp_paths[-1][-1]


bad = ["0 0 0 1","6 6 5 6"]
print distinct_paths(6,6,bad)
