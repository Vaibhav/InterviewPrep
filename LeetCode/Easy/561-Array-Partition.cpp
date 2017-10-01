// Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

class Solution {
public:
    
    int findMin(vector<int>& arr) {
        int min = arr[0];
        int len = arr.size();
        
        for(int i = 1; i < len; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;  
    }
    
    int arrayPairSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = nums.size() / 2; 
        int len = nums.size();
        int sum = 0, j = 0; 
        
        vector<int> tmp; 
        for(int i = 0; i < len; i++) {
            j++; 
            tmp.push_back(nums[i]);
            if (j == 2) {
                sum += findMin(tmp);
                tmp.clear();
                j = 0;
            }
        }
        return sum;
        
    }
};
