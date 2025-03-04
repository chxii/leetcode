#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def exchange(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            exchange(root.left)
            exchange(root.right)
        exchange(root)
        return root
# @lc code=end

