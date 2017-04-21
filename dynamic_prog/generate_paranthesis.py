#!/usr/bin/python


def main(n):
    result = []
    generate_paran("", 0, 0, n, result) 
    print result

def generate_paran(output, left, right, n, result):
    # scope to add left
    if left == right == n:
        result.append(output)
    else:
        if left < n:
            generate_paran(output+"(", left+1, right, n, result)
        if right < left:
            generate_paran(output+")", left, right+1, n, result) 

n = input("Enter the n of braces ")
main(n)
