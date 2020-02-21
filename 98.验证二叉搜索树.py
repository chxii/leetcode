#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Method 1:
        # def helper(node, lower = float('-inf'), upper = float('inf')):
        #     if not node:
        #         return True
            
        #     val = node.val
        #     if val <= lower or val >= upper:
        #         return False

        #     if not helper(node.right, val, upper):
        #         return False
        #     if not helper(node.left, lower, val):
        #         return False
        #     return True

        # return helper(root)

        # Method 2:
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True 
        

        
# @lc code=end

