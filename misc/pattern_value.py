#!/usr/bin/python


## Detect if a given pattern exists in a string/value
## Eg. aaba - catcatdogcat


def detectPattern(pattern, value):
    # first get the main char and maximum length
    if len(pattern) == 0: return len(value) == 0
    main_char = 'a' if pattern[0] == 'a' else 'b'
    alt_char = 'b' if main_char == 'a' else 'a'
    main_char_count_in_pattern = getCount(pattern, main_char)
    alt_char_count_in_pattern = getCount(pattern, alt_char)
    get_alt_char_first_index_pattern = pattern.index(alt_char)
    main_char_string_max_length = len(value)/main_char_count_in_pattern  # len/count
    for i in range(1,main_char_string_max_length+1):  # try different sizes
        main_string = value[:i]
        alt_string=''
        remaining_length = len(value)-(len(main_string)*main_char_count_in_pattern)
        if (remaining_length % alt_char_count_in_pattern) == 0:
            alt_string_size = remaining_length/alt_char_count_in_pattern
            alt_string_index = get_alt_char_first_index_pattern * i  # index * size of main
            alt_string = value[alt_string_index:alt_string_index+alt_string_size]
        if buildString(main_string, alt_string, pattern, value, main_char, alt_char):
            return True 
    return False

def buildString(mainString, altString, pattern, value, main_char, alt_char):
    print mainString, altString 
    bstring = ""
    for i in pattern:
        if i == main_char:
            bstring = bstring + mainString
        elif i == alt_char:
            bstring = bstring + altString
    if bstring == value:
        return True
    return False
    
def getCount(string, char):
    leng = 0
    for i in range(len(string)):
        if string[i] == char:
            leng += 1
    return leng

pattern = 'aaba'
value = 'catcatdogcat'
print detectPattern(pattern, value)
