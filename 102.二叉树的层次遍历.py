#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
            
        output = []

        def recur(curr, level):
            if level == len(output):
                output.append([])
            
            output[level].append(curr.val)
            
            if curr.left:
                recur(curr.left, level + 1)
            if curr.right:
                recur(curr.right, level + 1)
            
        recur(root, 0)
        return output

# @lc code=end

