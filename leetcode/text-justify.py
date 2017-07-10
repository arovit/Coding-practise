#!/usr/bin/python

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        running_len = 0
        running_sent = []
        for w in words:
            if len(w) + running_len + len(running_sent) > maxWidth:
                # cannot add w 
                for i in range(maxWidth - running_len):  ## they have to be divided equally RR
                    running_sent[i%(len(running_sent)-1 or 1)] += " "   # i% (number of words-1)
                result.append(''.join(running_sent))  # add to the final lislt
                running_sent = []                      # reinitialize running sent
                running_len = 0                 
            running_sent.append(w)
            running_len += len(w)
        result.append(' '.join(running_sent).ljust(maxWidth))
        return result
        
