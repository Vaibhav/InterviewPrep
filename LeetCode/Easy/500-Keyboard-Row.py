class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        
        for i in words:
            t = set(i.lower())
            if row1 & t == t:
                ret.append(i)
            if row2 & t == t:
                ret.append(i)
            if row3 & t == t:
                ret.append(i)
        return ret
