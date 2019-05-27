'''
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    cur_sum = 0
    
    def addNodeVal(self, node: TreeNode):
        if node is None:
            return None
        
        self.addNodeVal(node.right)
        node.val = node.val + self.cur_sum
        self.cur_sum = node.val 
        self.addNodeVal(node.left)
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return

        curTree = root
        self.addNodeVal(root)
        return curTree
