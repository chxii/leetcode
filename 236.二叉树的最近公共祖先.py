#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if p/q not found: return None
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, q, p)
        right = self.lowestCommonAncestor(root.right, q, p)

        if not left:
            return right
        if not right:
            return left
        return root
# @lc code=end

