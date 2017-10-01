class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num == 1) {
            return true;
        }
        for (int i = 0; i < (num / 2) + 1; i++) {
            if (i * i == num) {
                return true; 
            }
        }
        return false; 
    }
};