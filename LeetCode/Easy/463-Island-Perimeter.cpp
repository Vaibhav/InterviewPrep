'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. 

The grid is rectangular, width and height dont exceed 100. 

Determine the perimeter of the island.
'''

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int len1 = grid.size();
        int len2 = grid[0].size();
        int sum = 0; 
        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                
                if (grid[i][j] == 0) {
                    
                    if (i != 0) {
                        // can look up
                      if (grid[i - 1][j] == 1) {
                          sum++; 
                      }  
                    }
                    
                    if (i != len1 - 1) {
                        // can look down
                        if (grid[i + 1][j] == 1) {
                          sum++; 
                        }  
                    }
                    
                    if (j != 0) {
                        // can look left
                      if (grid[i][j-1] == 1) {
                          sum++; 
                      }  

                    }
                    
                    if (j != len2 - 1) {
                        // can look right 
                      if (grid[i][j+1] == 1) {
                          sum++; 
                      }  
                    }
                    
                } else {
                    if (i == 0) {
                          sum++; 
                    }
                    
                    if (i == len1 - 1) {
                          sum++; 
                    }
                    
                    if (j == 0) {
                          sum++; 
                    }
                    
                    if (j == len2 - 1) {
                          sum++; 
                    }   
                }              
            }
        }
        return sum; 
    }
};

