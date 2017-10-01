class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        int arrLen = nums.size();
        int i = 0; 
        for (i = 0; i < arrLen; i++) {
            if (target <= nums[i]) {
                return i; 
            }
        }
        
        return i; 
        
        
    }
};