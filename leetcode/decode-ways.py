class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        elif s[0] == '0':
            return 0
        count_ways = [0 for i in range(len(s)-1)]
        count_ways = [1,1]+count_ways
        for i in range(2, len(s)+1):
            count_ways[i] = 0
            if s[i-1] != '0':
                count_ways[i] = count_ways[i-1]
            if s[i-2] != '0' and (int(str(s[i-2:i])) <= 26):
                count_ways[i] += count_ways[i-2]
        print count_ways
        return count_ways[-1]
