#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        def maxProfit_k_inf(prices):
            dp_i_0, dp_i_1 = 0, -float('inf')
            for price in prices:
                temp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + price)
                dp_i_1 = max(dp_i_1, temp - price)
            return dp_i_0

        if k > n / 2:
            return maxProfit_k_inf(prices)
        
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for k in range(1, k+1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[n-1][k][0]
# @lc code=end

