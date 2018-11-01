class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: 
            return 0
        
        if x <= 3:
            return 1
        
        left = 1 
        right = x//2
        
        if right*right == x:
            return right
        
        while(True):
            mid = left + (right-left)//2
            
            if (mid*mid > x):
                right = mid - 1
            elif (mid*mid == x or (mid+1)*(mid+1) > x):
                return mid
            else:
                left = mid + 1