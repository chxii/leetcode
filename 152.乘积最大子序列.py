#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        x = 0 # 表示前一个负数存在的地方
        for i in range(1, n):
            if nums[i] > 0:
                dp[i] = max(dp[i - 1] * nums[i], nums[i])
            else:
                if dp[x - 1] > 0:
                    temp = dp[x - 1]
                else:
                    temp = 1
                while x < i:
                    temp = temp * nums[x]
                    x += 1
                dp[i] = max(temp * nums[i], nums[i])
        return max(dp)

        # solution2:
        # 由于存在负数，那么会导致最大的变最小的，最小的变最大的。
        # 因此还需要维护当前最小值imin，
        # imin = min(imin * nums[i], nums[i])
        # 当负数出现时则imax与imin进行交换再进行下一步计算

# @lc code=end

