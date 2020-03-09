#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or len(obstacleGrid) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n] * m
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        if obstacleGrid[m-1][n-2] == 0:
            dp[m-1][n-2] = 1
        if obstacleGrid[m-2][n-1] == 1:
            dp[m-2][n-1] = 1
        
        dp[m-1] = [1] * n
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif j + 1 < n and i + 1 < m:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j]
                elif j + 1 < n:
                    dp[i][j] = dp[i][j+1]
                elif i + 1 < m:
                    dp[i][j] = dp[i+1][j]
        # print(dp)
        return dp[0][0]
# @lc code=end

