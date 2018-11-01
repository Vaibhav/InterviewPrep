class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2: 
            return [[1],[1,1]]
        
        triangle = [
            [1],
            [1,1]
        ]
        
        for i in range(1,numRows-1):
            prev = triangle[i]
            x = [0] * (i+2)
            x[0] = 1
            x[-1] = 1
            
            for j in range(1,i+1):
                x[j] = triangle[i][j] + triangle[i][j-1]
            
            triangle.append(x)
        

        return triangle