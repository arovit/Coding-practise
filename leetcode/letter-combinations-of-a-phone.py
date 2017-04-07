#!/usr/bin/python

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.hash_code = { '0': ' ',
			   '1': '*',
			   '2': 'abc',
			   '3': 'def',
			   '4': 'ghi',
			   '5': 'jkl',
			   '6': 'mno',
			   '7': 'pqrs',
			   '8': 'tuv',
			   '9': 'wxyz' }
        if not digits:
            return []
        result = list(self.hash_code[digits[0]])
        for i in digits[1:]:
            result = self.combination(result, i) 
        return result
 
    def combination(self, result, number):
        new_list = []
        for index, val in enumerate(result):
            for i in self.hash_code[number]:
                new_list.append(val+i)
        return new_list

sol = Solution()
num = raw_input('Enter the number').strip()
print sol.letterCombinations(num)
