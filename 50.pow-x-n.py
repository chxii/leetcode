#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return math.pow(x, n)

        # 分治思想
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        b = self.myPow(x, n//2)
        l = self.myPow(x, n%2)
        return b * b * l
        
# @lc code=end

