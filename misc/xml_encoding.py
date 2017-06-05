#!/usr/bin/python

import xml.etree.ElementTree



keywordMap = {}

encoded_string = ""
root = ET.fromstring(xml_string)
encode_element(root, encoded_string)


def encode_element(element, estring):
    etag = keywordMap.get(element.tag, 'UNKNOWN')
    estring += " %s"%etag # add tag  
    for i in element.attrib:
        eattrib = keywordMap.get(i, 'UNKNOWN'):
        estring += " %s"%eattrib # add attrib 
        estring += element.attrib[i]  
    estring += " 0"
    if element.text:
        estring += " %s"%element.text
    for child in element:
        encode_element(child)
    estring = estring + " 0"
    




