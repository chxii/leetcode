#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                output += prices[i+1] - prices[i]
        return output
# @lc code=end

