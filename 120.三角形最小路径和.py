#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle) == 0:
            return 0
        m = len(triangle)
        n = len(triangle[-1])
        dp = [[float('inf')] * (n) for _ in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i+1):
                # print(i, j)
                if j - 1 >= 0:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                else:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
        return min(dp[-1])

# @lc code=end

