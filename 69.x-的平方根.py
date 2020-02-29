#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        left = 1
        right = x
        while left <= right:
            # print(left, right)
            mid = math.floor((left + right) / 2)
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
# @lc code=end

