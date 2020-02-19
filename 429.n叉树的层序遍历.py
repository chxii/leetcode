#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []

        def traversal(root, level):
            if not root:
                return
            if len(output) == level:
                output.append([])
            output[level].append(root.val)
            for i in root.children:
                traversal(i, level+1)          
        
        traversal(root, 0)
        return output

        ##### DFS:
        # if root is None:
        # return []        

        # result = []
        # previous_layer = [root]

        # while previous_layer:
        #     current_layer = []
        #     result.append([])
        #     for node in previous_layer:
        #         result[-1].append(node.val)
        #         current_layer.extend(node.children)
        #     previous_layer = current_layer
        # return result

# @lc code=end

