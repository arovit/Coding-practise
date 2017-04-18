#!/usr/bin/python
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        char_index = 0 
        found_index = []
        if words:
            word_len = len(words[0])
        else:
            return found_index
        for i in xrange(0,len(s)-(len(words)*word_len) + 1):
            char_index = 0
            while char_index < word_len:
                form_list = []
                for j in range(len(words)):
                    form_list.append(words[j][char_index])
                print form_list
                for j in range(len(words)):
                    check_ind = i + char_index + (word_len * j)
                    if s[check_ind] != form_list[j]:
                        char_index = word_len + 1  ## Break while loop
                        break
                else:
                    char_index  += 1
            if char_index == word_len:
                found_index.append(i) 
        return found_index

sol = Solution()
print sol.findSubstring("abaababbaba",['ab','ba','ab','ba'])
