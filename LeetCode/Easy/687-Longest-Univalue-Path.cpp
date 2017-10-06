// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};



class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        int ans = 0;
        if (root) dfs(root, ans);
        return ans;
    }

private:
    int dfs(TreeNode* node, int& count) {
        int l = node->left ? dfs(node->left, count) : 0;
        int r = node->right ? dfs(node->right, count) : 0;
        int left_result = node->left && node->left->val == node->val ? l + 1 : 0;
        int right_result = node->right && node->right->val == node->val ? r + 1 : 0;
        count = max(count, left_result + right_result);
        return max(left_result, right_result);
    }
};
