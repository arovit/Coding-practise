#!/usr/bin/python


str1 = 'arovitnarul'
str2 = 'aro'
str3 = 'parularo'


def replace_str(main_str, from_str, to_str):
    index = 0 
    flen = len(from_str)
    while index < len(main_str):
        if main_str[index:index+flen] == from_str:
            main_str = do_replace(main_str, index, index+flen, to_str) 
        index += 1 
    return main_str

def do_replace(main_str, sindex, eindex, to_str):
    main_str = main_str[:sindex] + to_str + main_str[eindex:]
    return main_str


print replace_str(str1, str2, str3)        
