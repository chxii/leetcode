#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_i_0, dp_i_1 = 0, -float('inf')
        for price in prices:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price - fee)
            dp_i_1 = max(dp_i_1, temp - price)
        return dp_i_0
        
# @lc code=end

