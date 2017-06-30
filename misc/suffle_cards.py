#!/usr/bin/python

import random

# shuffle deck of 52 cards
def shuffle_list(card_list, indx):
    if indx == 0:
        return 
    shuffle_list(card_list, indx-1)
    k = random.randint(0,indx) # choose a card to be swapped with
    card_list[k], card_list[indx] = card_list[indx], card_list[k]  
    return



cards = [1,2,3,4,5,6]
shuffle_list(cards, len(cards)-1)
print cards
