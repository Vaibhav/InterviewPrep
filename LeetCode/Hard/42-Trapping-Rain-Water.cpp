

/* 

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

*/

#include <iostream>
#include <vector>


class Solution {
public:
    int trap(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int level = 0;
        int water = 0;
        
        while (i < j) {
            int lower = height[height[i] < height[j] ? i++ : j--];
            level = max(level, lower);
            water += level - lower;
            
        }
        
        return water;
    }
};
