#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def gp(s, left, right):
            if right == 0:
                output.append(s)
                return 
            if left != 0:
                gp(s+"(", left - 1, right)
            if right > left:
                gp(s+")", left, right - 1)
        gp( "", n, n)
        return output
    
    
        
        
# @lc code=end

