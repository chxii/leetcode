#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        value = preorder.pop(0) # change the length of preorder
        idx = inorder.index(value)
        node = TreeNode(value)

        node.left = self.buildTree(preorder[:idx], inorder[:idx])
        node.right = self.buildTree(preorder[idx:], inorder[idx+1:])

        return node
        
# @lc code=end

