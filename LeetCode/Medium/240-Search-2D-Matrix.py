'''
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if matrix == []:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        col = 0
        row = m - 1 
        
        while col < n and row > -1:
            elem = matrix[row][col]
            if elem == target: 
                return True
            elif elem < target:
                col += 1
            else:
                row -= 1
        
        return False