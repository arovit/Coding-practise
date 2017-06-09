#!/usr/bin/python

expense_list = [1,2,3,4,5] 

from collections import OrderedDict
def whoGivesWhom(expense_list):
    eq_amount = sum(expense_list)/len(expense_list)
    to_give = OrderedDict()
    to_receive = OrderedDict()
    for index,i in enumerate(expense_list):
        if i > eq_amount: # he paid more
            to_receive[index] = i-eq_amount
        elif eq_amount > i:
            to_give[index] = eq_amount-i
    index_to_give = 0
    index_to_receive = 0
    #print to_give
    #print to_receive
    while index_to_give < len(to_give.keys()):
        if to_give[to_give.keys()[index_to_give]] > to_receive[to_receive.keys()[index_to_receive]]:
            to_give[to_give.keys()[index_to_give]] = to_give[to_give.keys()[index_to_give]] - to_receive[to_receive.keys()[index_to_receive]]
            print "%s gave %s %s dollars"%(to_give.keys()[index_to_give], to_receive.keys()[index_to_receive], to_receive[to_receive.keys()[index_to_receive]])
            index_to_receive += 1 
        elif to_give[to_give.keys()[index_to_give]] < to_receive[to_receive.keys()[index_to_receive]]:  # to_receive > to_give
            to_receive[to_receive.keys()[index_to_receive]] = to_receive[to_receive.keys()[index_to_receive]] - to_give[to_give.keys()[index_to_give]]
            print "%s gave %s %s dollars"%(to_give.keys()[index_to_give], to_receive.keys()[index_to_receive], to_give[to_give.keys()[index_to_give]])
            index_to_give += 1
        else:
            print "%s gave %s %s dollars"%(to_give.keys()[index_to_give], to_receive.keys()[index_to_receive], to_give[to_give.keys()[index_to_give]])
            index_to_give += 1
            index_to_receive += 1  
        #print index_to_receive
        #print index_to_give 
     
    
whoGivesWhom(expense_list)
