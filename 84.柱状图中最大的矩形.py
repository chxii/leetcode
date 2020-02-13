#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if (len(heights)==0):
            return 0
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while left < right:
            maxArea = max(maxArea, (right-left+1)*min(heights[left:right+1]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        
        
# @lc code=end

