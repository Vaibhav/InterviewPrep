class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        map<int, int> m;
        vector<int> ret; 
        int len = nums.size(); 
        for (int i = 0; i < len; i++) {
            if (m.count(nums[i]) > 0) {
                m[nums[i]]++;
                ret.push_back(nums[i]);
            } else {
                m[nums[i]] = 1;
            }
        }
        return ret;
    }
};
