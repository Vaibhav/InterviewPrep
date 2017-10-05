#include <math.h>

class Solution {
public:
    bool judgeSquareSum(int c) {
        for (int i = 0; i <= int(sqrt(c)); i++){
            if(floor(sqrt(c-i*i)) == sqrt(c-i*i)){
                return true;
            }
        }
        return false; 
    }
};
