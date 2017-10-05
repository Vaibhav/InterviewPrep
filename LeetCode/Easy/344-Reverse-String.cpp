class Solution {
public:
    string reverseString(string s) {
        int n = s.length();
        char tmp; 
        for (int i = 0, j = n - 1; i < n/2; i++, j--) {
            tmp = s[j];
            s[j] = s[i];
            s[i] = tmp;
        }
        return s;
    }
};
