#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost)

        dp = [0] * (n + 1)
        cost.append(0)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-1], dp[-2])
        
# @lc code=end

