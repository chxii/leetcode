#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # n = len(stones)
        # dp = [False] * (stones[-1] + 1)
        # dp[0] = True
        
        def recur(idx, stone_idx, k):
            if idx == stones[-1]:
                return True
            if idx > stones[-1] or stone_idx == len(stones) - 1:
                return False
            if idx + k in stones:
                recur(idx+k, stones.index(idx+k), k)
            elif idx + k - 1 in stones:
                recur(idx+k-1, stones.index(idx+k-1), k-1)
            elif idx + k + 1 in stones:
                recur(idx+k+1, stones.index(idx+k+1), k+1)
        
        return recur(1, 1, 1)

                
        
# @lc code=end

