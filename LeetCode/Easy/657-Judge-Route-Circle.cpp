/*
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
*/

class Solution {
public:
    bool judgeCircle(string moves) {
        int horiz = 0, vert = 0; 
        int len = moves.length(); 
        
        for (int i = 0; i < len; i++) {
            if (moves[i] == 'U') {
                vert++;
            } else if (moves[i] == 'D') {
                vert--;
            } else if (moves[i] == 'L') {
                horiz--;
            } else if (moves[i] == 'R') {
                horiz++;
            }
        }
        
        if (horiz == 0 && vert == 0) {
            return true;
        } else {
            return false;
        }
    }
};