'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

class Solution(object):
    def climbStairs(self, n):
        mapa = {}
        def climbStairsDP(n, dat):
            """
            :type n: int
            :rtype: int
            """
            if(n <= 0):
                return 1
            a,b = 0,0
            if(n >= 1):
                if(dat.get(n-1) is not None):
                    a = dat[n-1]
                else:
                    dat[n-1] = climbStairsDP(n-1, dat)
                    a = dat[n-1]
            if(n >= 2):
                if(dat.get(n-2) is not None):
                    b= dat[n-2]
                else:
                    dat[n-2] = climbStairsDP(n-2, dat)
                    b = dat[n-2]
            return a+b
        
        return climbStairsDP(n, mapa)   