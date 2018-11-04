'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cols = len(grid[0])
        rows = len(grid)
        ans = [] 
        for i in range(rows):
            ans.append([0] * cols)
        
        ans[0][0] = grid[0][0]

        for i in range(rows): 
            for j in range(cols):
                if i != 0 and j == 0: 
                    ans[i][j] = grid[i][j] + ans[i-1][j]
                elif i == 0 and j != 0: 
                    ans[i][j] = grid[i][j] + ans[i][j-1]
                elif i != 0 and j != 0:
                    ans[i][j] = grid[i][j] + min(ans[i-1][j], ans[i][j-1])

        return ans[rows-1][cols-1]