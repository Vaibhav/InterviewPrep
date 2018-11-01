'''
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example:
Input: "123"
Output: "121"

Note:
    The input n is a positive integer represented by string, whose length will not exceed 18.
    If there is a tie, return the smaller one as answer.
'''


class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        num = int(n)
        
        # Generates 99...99 and 100...001
        candidates = [str(10**k + diff) for k in (length-1, length) for diff in (-1, 1)]

        
        prefix = n[:(length+1)//2]
        pre = int(prefix)
        prefixDiff = [str(pre-1), str(pre), str(pre+1)]
        
        for start in prefixDiff:
            # If number is even length, need to reverse whole prefix, 
            # else you don't need to include last element in preix (as this will be the middle element)
            candidates.append(start + (start[:-1] if length%2 else start)[::-1])
    
        # print(candidates)
        
        def delta(x):
            return abs(num - int(x))

        # Loop through and find smallest palindrome by comapring delta of each number in list against n
        ans = None
        for cand in candidates:
            if cand != n:
                if (ans is None or delta(cand) < delta(ans) or (delta(cand) == delta(ans) and int(cand) < int(ans))):
                    ans = cand
        return ans
        