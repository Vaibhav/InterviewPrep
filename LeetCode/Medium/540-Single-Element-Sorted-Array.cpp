class Solution {
public:
    int singleNonDuplicate(vector<int>& nums)
    {

        int len = nums.size();
        int ret = 0;

        for (int i = 0; i < len; i++) {
            if (i + 1 < len && (nums[i] != nums[i + 1] && nums[i] != nums[i - 1])) {
                return nums[i];
            }
            else if (i + 1 >= len && (nums[i] != nums[i - 1])) {
                return nums[i];
            }
        }

        return ret;
    }
};
