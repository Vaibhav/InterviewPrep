class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLen = 0
        used = {}
        
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start + 1)

            used[s[i]] = i

        return maxLen
