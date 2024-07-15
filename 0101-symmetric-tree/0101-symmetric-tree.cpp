/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    bool symmetric(TreeNode*left, TreeNode* right){ 
        if(!left && !right) return true;
        if(left && !right || !left && right) return false;
        return left->val == right -> val && \ 
        symmetric(left -> left, right -> right) && symmetric(left -> right, right -> left);
    }

public:
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return symmetric(root->left, root->right);
        
        

    }
};