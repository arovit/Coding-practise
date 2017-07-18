#!/usr/bin/python 
mdict = {
	'1':'a',
	'2':'b',
	'3':'c',            
 	'4': {
		'1':'a',
		'2':{
			'1':'a',
		    }
 	     }
         }


def print_value(ndict, target):
    rkeys = []
    for i in ndict.keys():
        if type(ndict[i]) == dict:
            keys_target = print_value(ndict[i], target) # this will return keys containing target
            for k in keys_target:
                rkeys.append('%s.%s'%(i,k))
        elif ndict[i] == target:
            rkeys.append(i)
    return rkeys 


print print_value(mdict, 'a')
