#!/usr/bin/python


def anotateWithNumCharacterPlaceholder(text):
    n = len(text)
    if n <= 0: return [""]
    result = [str(n)]
    for k in range(1, n - 1):
        pfx = str(k) + text[k : k + 1]
        for sfx in anotateWithNumCharacterPlaceholder(text[k + 1 :]):
            result.append(pfx + sfx)
    
    pfx = text[:1]
    for sfx in anotateWithNumCharacterPlaceholder(text[1:]):
        result.append(pfx + sfx)
    return result


print anotateWithNumCharacterPlaceholder('abc')
