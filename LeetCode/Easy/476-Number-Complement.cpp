class Solution {
public:
    int findComplement(int num) {
        int mask = num;
        mask = (mask >> 1) | mask;
        mask = (mask >> 2) | mask;
        mask = (mask >> 4) | mask;
        mask = (mask >> 8) | mask;
        mask = (mask >> 16) | mask;
        return num ^ mask;
    }
};
