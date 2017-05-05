#!/usr/bin/python


# group by anagrams

def gp_anagrams(list_words):
    hash_words = {}
    output_list = []
    for i in list_words:
        keyw = "".join(sorted(i))
        rlist = hash_words.get(keyw,[])
        rlist.append(i)
        hash_words[keyw] = rlist
    for i in hash_words:
        output_list.extend(hash_words[i])
    print output_list


lwords = ['aro','ora','rao','vit','tib','bit','oid','fig']
gp_anagrams(lwords)
