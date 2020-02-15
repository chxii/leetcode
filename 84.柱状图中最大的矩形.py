#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maxArea = 0
        # for i in range(len(heights)):
        #     left = i-1
        #     while left >= 0 and heights[left] >= heights[i]:
        #         left -= 1
        #     right = i+1
        #     while right < len(heights) and heights[right] >= heights[i]:
        #         right += 1
        #     width = right - left - 1
        #     currArea = width * heights[i]
        #     maxArea = max(maxArea, currArea)
        # return maxArea

        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)): 
            while stack and heights[stack[-1]] > heights[i]:               
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res
        
        
# @lc code=end

