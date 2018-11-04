'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

'''

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # robbery of current house + loot from houses before the previous
        # loot from the previous house robbery and any loot captured before that
        # rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
        
        length = len(nums)
        
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0],nums[1])
        
        curPrev = 0
        prev = 0
        for i in range(0,length-1):
            tmp = curPrev
            curPrev = max(curPrev, prev + nums[i])
            prev = tmp
        
        curPrev2 = 0
        prev2 = 0
        length = len(nums)
        for i in range(1,length):
            tmp = curPrev2
            curPrev2 = max(curPrev2, prev2 + nums[i])
            prev2 = tmp
            
        return max(curPrev, curPrev2)
        