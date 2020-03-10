#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def getMax(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]       
            dp[1] = max(nums[1], nums[0])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
            return dp[-1]
        
        return max(getMax(nums[:len(nums)-1]), getMax(nums[1:]))

        # 简洁的写法
        # def my_rob(nums):
        #     cur, pre = 0, 0
        #     for num in nums:
        #         cur, pre = max(pre + num, cur), cur
        #     return cur
        # return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

# @lc code=end

