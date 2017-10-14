class Solution {
public:
    void reverseWords(string &s) {
        if(s.empty()) return;
        
        int len1 = s.size();
        int l=0;
        
        for(int i = 0; i < len1; i++) {
            if(s[i] != ' ' || (i > 0 && s[i-1] != ' '))
                s[l++] = s[i];
        }
        
        if (l > 0 && s[l-1] == ' ') l--;
        s = s.substr(0,l);
        if (s.empty()) return;
        
        reverse(s.begin(), s.end());
        
        l = 0;
        int len2 = s.size();
        for(int i = 0;i < len2; i++) {
            
            if(s[i] == ' ') {
                reverse(s.begin()+l, s.begin()+i);
                l = i+1;
            }
        }
        
        reverse(s.begin()+l, s.end());
    }
};
