#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        q = [(root, 0)]
        while q:
            curr, level = q.pop(0)
            if level == len(result):
                result.append(curr.val)
            result[level] = max(result[level], curr.val)
            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))
            
        return result

        
# @lc code=end

