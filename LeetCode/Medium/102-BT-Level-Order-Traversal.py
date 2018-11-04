'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        out = []
        queue = collections.deque()
        queue.append((root,0)) # (node,level)

        while queue:
            root,level = queue.popleft()
            if root:
                if root.left is not None:
                    queue.append((root.left,level+1))
                if root.right is not None:
                    queue.append((root.right,level+1))
                if len(out) < level+1:
                    out.append([])
                out[level].append(root.val)
        return out