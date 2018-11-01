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


    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
            
        for i, cur_chars in enumerate(zip(*strs)):
            # Loops through each letter of each word in strs
            # print(i, cur_chars)
            # cur_chars is tuple of chars of each word
            if len(set(cur_chars)) > 1:
                return strs[0][:i]
        else:
            return min(strs)