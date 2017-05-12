#!/usr/bin/python

#random_list = [3,2,3,4,5,6,1,2,2]
random_list = [5,3,1,2,3]

def classify_peaks_valleys(random_list):
    index = 0
    while (index < len(random_list)) and (index+1 < len(random_list)):
        if index % 2 == 0: ## find desc sequence
            if random_list[index+1] > random_list[index]:
                random_list[index+1], random_list[index] = random_list[index], random_list[index+1] 
        if index % 2 == 1: ## find asc sequence
            if random_list[index+1] < random_list[index]:
                random_list[index+1], random_list[index] = random_list[index], random_list[index+1] 
        index += 1
    print random_list


classify_peaks_valleys(random_list)
