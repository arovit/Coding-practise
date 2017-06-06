#!/usr/bin/python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """ 
        self.memoize = {}
        return self.matchWords(word1, word2)
    
    def matchWords(self, word1, word2):
        if self.memoize.get((word1,word2)):
            return self.memoize[(word1, word2)]
        if word1 and not word2:
            ret =  len(word1)
        elif word2 and not word1:
            ret = len(word2)
        elif (not word1) and (not word2):
            ret = 0
        else:
            if word1[0] == word2[0]:
                ret = self.matchWords(word1[1:], word2[1:])
            else:
                # try replace
                rcount = self.matchWords(word1[1:], word2[1:])
                icount = self.matchWords(word1, word2[1:])
                dcount = self.matchWords(word1[1:], word2)
                ret = min(rcount, icount, dcount) + 1
        print "word1 %s, word2 %s - count %s"%(word1, word2, ret) 
        self.memoize[(word1, word2)] = ret
        return ret


sol = Solution()
print sol.minDistance('park', 'spake')

                
