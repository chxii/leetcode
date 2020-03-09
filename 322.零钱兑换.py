#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # greedy + dfs
        # def recur(amount, idx, count, ans):
        #     if amount == 0:
        #         ans[0] = min(ans[0], count)
        #         return
        #     if idx == len(coins):
        #         return
        #     for k in range(amount // coins[idx], -1, -1):
        #         if k + count < ans[0]:
        #             recur(amount - k * coins[idx], idx + 1, count + k, ans)
        
        # if amount == 0:
        #     return 0
        # coins.sort()
        # ans = [float('inf')]
        # recur(amount, 0, 0, ans)
        # if ans[0] == float('inf'):
        #     return -1
        # return ans[0]

        # dp solution
        # @functools.lru_cache(amount)
        # def dp(rem):
        #     if rem < 0: return -1
        #     if rem == 0: return 0
        #     mini = int(1e9)
        #     for coin in self.coins:
        #         res = dp(rem - coin)
        #         if res >= 0 and res < mini:
        #             mini = res + 1
        #     return mini if mini < int(1e9) else -1

        # self.coins = coins
        # if amount < 1: return 0
        # return dp(amount)
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 



        
# @lc code=end

