#!/usr/bin/python

wordlist = ['hi','is', 'this', 'is', 'hello', 'world','arovit', 'is']
def word_distance(word1, word2, wordlist):
    index1 = -1
    index2 = -1
    min_dis = 999
    for i in range(len(wordlist)):
        if word1 != word2:
            if wordlist[i] == word1:
                index1 = i
            elif wordlist[i] == word2:
                index2 = i    
        else:
           if wordlist[i] == word1:
               if index1 > index2:
                   index2 = i
               else:
                   index1 = i
        if index1 >= 0 and index2 >=0:
            min_dis = min(min_dis, abs(index1-index2)) 
    return min_dis

print word_distance('is','is', wordlist)



def word_distance_2(word1, word2, wordlist):
    word_index_hash = {}
    for index, value in enumerate(wordlist):
        temp = word_index_hash.get(value,[])
        temp.append(index)
        word_index_hash[value] = temp
    print word_index_hash
    list1 = word_index_hash[word1]
    list2 = word_index_hash[word2]
    i = j = 0
    min_distance = 999
    while (i < len(list1) and j < len(list2)):
        min_distance = min(min_distance, abs(list1[i]-list2[j]))   
        if list1[i] > list2[j]:
            j += 1
        else:
            i += 1
    return min_distance

print word_distance_2('is','arovit',wordlist)

