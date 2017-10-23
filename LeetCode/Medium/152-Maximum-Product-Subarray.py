class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        n = len(nums)
        imax = ret
        imin = ret
        if n == 0 or n == 1:
            return ret 
        
        for i in range(1,n): 
            
            if nums[i] < 0:
                imax, imin = imin, imax
            
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])
            
            ret = max(ret, imax)
        
        return ret
