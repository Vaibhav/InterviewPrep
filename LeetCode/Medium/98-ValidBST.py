import sys
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def BSTValid(self, node, min_val, max_val):
        
        if node is None:
            return True
        elif node.val < min_val or node.val > max_val:
            return False
        
        left_valid = self.BSTValid(node.left, min_val, node.val-1)
        right_valid = self.BSTValid(node.right, node.val+1, max_val)
        
        return left_valid and right_valid
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.BSTValid(root,-sys.maxsize,sys.maxsize)
