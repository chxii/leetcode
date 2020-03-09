#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        for row in dp:
            row[n-1] = 1
        dp[m-1] = [1] * n
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        # print(dp)
        return dp[0][0]

# @lc code=end

