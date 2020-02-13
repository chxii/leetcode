#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            if i == ')' and (not stack or stack.pop() != '('):
                return False
            if i == '}' and (not stack or stack.pop() != '{'):
                return False
            if i == ']' and (not stack or stack.pop() != '['):
                return False
        if len(stack) != 0:
            return False
        return True
                
        
# @lc code=end

