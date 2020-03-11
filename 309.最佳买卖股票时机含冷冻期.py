#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][k][0 or 1]
        # 0 <= i <= n-1, 1 <= k <= K
        # n 为天数，大 K 为最多交易数, 1 表示持有，0 表示没有持有
        # 此问题共 n × K × 2 种状态，全部穷举就能搞定


        # base case：
        # dp[-1][k][0] = dp[i][0][0] = 0
        # dp[-1][k][1] = dp[i][0][1] = -infinity

        # 状态转移方程：
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        # for this problem: k = inf
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        dp_i_0, dp_i_1 = 0, -float('inf')
        dp_i2 = 0 # dp[i-2][0]
        for price in prices:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, dp_i2 - price)
            dp_i2 = temp
        return dp_i_0
        
# @lc code=end

