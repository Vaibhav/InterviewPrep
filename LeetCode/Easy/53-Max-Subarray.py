class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsofar = nums[0]
        maxsuffixsum = nums[0]
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) < 1:
            return 0
        
        for i in range(1,len(nums)):
            maxsuffixsum = max(nums[i], maxsuffixsum + nums[i])
            # print(maxsuffixsum)
            maxsofar = max(maxsofar, maxsuffixsum)

        return(maxsofar)