#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ## Method 1:
        # output = []
        
        # def traversal(root):
        #     if not root:
        #         return        
        #     for i in root.children:
        #         traversal(i)
        #     output.append(root.val)
            
        
        # traversal(root)
        
        # return output

        ## Method 2:
        if root is None:
            return []
        
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
                
        return output[::-1]

        
# @lc code=end

