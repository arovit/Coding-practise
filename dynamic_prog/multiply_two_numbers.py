#!/usr/bin/python


def rmultiply(num1, num2):
    if num1 == 1:
        return num2
    elif num2 == 1:
        return num1
    if num1 %2 == 0:
        result = rmultiply(num1/2, num2)
        result = result << 1
    elif num2 %2 == 0:
        result = rmultiply(num1, num2/2)
        result = result << 1
    else:
        num1 = num1 - 1
        result = rmultiply(num1, num2)
        result = result + num2
    return result

array = map(int, raw_input("Enter 2 nums ").strip().split(' '))
print rmultiply(array[0], array[1])
