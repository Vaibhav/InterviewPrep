class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def pali(s):
            if s == s[::-1]:
                return True
            return False
        
        if s == "" or len(s) == 1:
            return s
        
        maxLen = 1
        start = 0
        length = len(s)
        for i in range(length):
        	if i - maxLen >= 1 and pali(s[i-maxLen-1:i+1]):
        		start = i - maxLen - 1
        		maxLen += 2
        		continue

        	if i - maxLen >= 0 and pali(s[i-maxLen:i+1]):
        		start = i - maxLen
        		maxLen += 1
                
        return s[start:start+maxLen]
