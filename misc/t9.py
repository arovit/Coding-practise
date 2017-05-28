#!/usr/bin/python

word_dict = { '1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz' }

words = ["to","the","uid","arovit","aim","narula","give","hello","world"]

def getNumber(char):
    """ can be optimised """
    for i in range(1,10):
        if char in word_dict[str(i)]:
            return str(i) 


class Node(object):
    def __init__(self):
        self.childDict = {}   # Dictionary of char: 'char': ChildNode eg. {'a': Node, 'b': Node, 'c'.... }
        self.endMarker = False
    def __str__(self):
        temp = ""
        for i in self.childDict:
            temp += "%s -> %s\n"%(i, self.childDict[i])
        return temp

## Ready the trie data structure
root = Node()
def pushInTrie(string, node):
    if not string:
        return
    lastchar = False
    if len(string) == 1:
        lastchar = True
    if string[0] not in node.childDict:
        child = Node()
        if lastchar: child.endMarker = True
        node.childDict.update({string[0]:child})
        pushInTrie(string[1:], child)
    else: # string[0] in node.childDict          
        node = node.childDict[string[0]]
        if lastchar: node.endMarker = True
        pushInTrie(string[1:], node) 
for i in words:
    pushInTrie(i, root)
           
def getAllStrings(node, prefix):
    if node.endMarker:
        print prefix
    for i in node.childDict:
        getAllStrings(node.childDict[i], prefix+i) 
###    


input_number = "843"

def get_all_words(input_number, prefix, node):
    if not input_number:
        if node.endMarker:
            print prefix
            return
    char_maps = word_dict[input_number[0]]
    for chr in char_maps:
        if chr in node.childDict:
            get_all_words(input_number[1:], prefix+chr ,node.childDict[chr])
        

get_all_words(input_number, '', root)
