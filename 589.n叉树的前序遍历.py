#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        # output = []
        
        # def traversal(root):
        #     if not root:
        #         return 
        #     output.append(root.val)       
        #     for i in root.children:
        #         traversal(i)          
        
        # traversal(root)
        
        # return output

        ## Method 2:
        if root is None:
            return []
        
        stack, output = [root, ], []            
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
                
        return output

        
# @lc code=end

