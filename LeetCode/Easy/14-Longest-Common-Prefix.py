# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ss = zip(*strs)
        ret = ""
        for c in ss:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret