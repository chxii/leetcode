#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = 0
        while left < right:
            ans = max(ans, (right-left)*min(height[left], height[right]))
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return ans

# @lc code=end

