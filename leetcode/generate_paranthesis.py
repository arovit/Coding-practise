class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.resultant = []
        self.brackets("", 0, 0, n)
        return self.resultant    
        
    def brackets(self,output, open, close, n):
        if open == close == n:
            self.resultant.append(output)
        else:
            if open < n:
                self.brackets(output+"(", open + 1, close, n)
            if close < open:
                self.brackets(output+")", open, close+1, n)
