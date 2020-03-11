#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
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

        dp_i10, dp_i11 = 0, -float('inf')
        dp_i20, dp_i21 = 0, -float('inf')
        for price in prices:
            dp_i10 = max(dp_i10, dp_i11 + price)
            dp_i11 = max(dp_i11, -price)
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
        
        return dp_i20


# @lc code=end

