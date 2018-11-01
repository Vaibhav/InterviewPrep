'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

'''

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        
        l1 = len(s)
        l2 = len(t)
        if (l1 != l2):
            return False
        
        for i in range(l1):
            j = s[i]
            k = t[i]
            dic[j] = dic.get(j,0) + 1
            dic[k] = dic.get(k,0) - 1
        
        x = list(dic.values())
    
        for i in x: 
            if i != 0:
                return False
        
        return True