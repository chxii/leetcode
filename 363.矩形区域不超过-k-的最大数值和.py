#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # m = len(matrix)
        # n = len(matrix[0])
        # dp = [[0] * (n+1) for _ in range(m+1)]
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]
        # # print(dp)
        # output = -float('inf')
        # for i1 in range(m):
        #     for i2 in range(i1+1, m+1):
        #         for j1 in range(n):
        #             for j2 in range(j1+1, n+1):
        #                 total = dp[i2][j2] - dp[i2][j1] - dp[i1][j2] + dp[i1][j1]
        #                 if total == k:
        #                     return total
        #                 if total < k:
        #                     output = max(output, total)
        
        # return output

        def maxSubArraylessK(nums, k):       
            cumset = [0]
            maxsum = -1<<32
            cursum = 0
            for i in range(len(nums)):
                cursum += nums[i]
                idx = bisect.bisect_left(cumset, cursum - k)
                if 0 <= idx < len(cumset):
                    maxsum = max(maxsum, cursum - cumset[idx])
                if maxsum == k:
                    break
                bisect.insort(cumset, cursum)
            return maxsum
               
        row, col = len(matrix), len(matrix[0])
        res = -(1<<32)
        for left in range(col):
            cursums = [0 for _ in range(row)]
            right = left
            while right < col:
                for i in range(row):
                    cursums[i] += matrix[i][right]
                curarrmax = maxSubArraylessK(cursums, k)
                res = max(res, curarrmax)
                right += 1
                
        return res
        
# @lc code=end

