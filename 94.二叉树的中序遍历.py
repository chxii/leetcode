#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        
        def traversal(root):
            if not root:
                return        
            traversal(root.left)
            output.append(root.val)
            traversal(root.right)
            
        
        traversal(root)
        
        return output
            
        
# @lc code=end

