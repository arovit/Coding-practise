#!/usr/bin/python


def edit_distance(word1, word2):
    if len(word1) == 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)
    else:
        # word1 and word2 exist
        if word1[0] == word2[0]:
            return edit_distance(word1[1:], word2[1:]) 
        else:
            r = edit_distance(word1[1:], word2[1:])
            i = edit_distance(word1, word2[1:])
            d = edit_distance(word1[1:], word2)
            return min(r, d, i) + 1




print edit_distance('arokit','arov')
