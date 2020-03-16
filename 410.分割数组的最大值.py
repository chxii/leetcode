#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
from itertools import combinations
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     dp[i] = dp[i-1] + nums[i]
        
        # output = float('inf')
        # for comb in combinations(range(1,len(nums)), m-1):
        #     # print(comb)
        #     max_sub_sum = 0
        #     for i in range(len(comb) + 1):
        #         if i == 0:
        #             idx1 = 0
        #         else: 
        #             idx1 = comb[i-1]
                
        #         if i == len(comb):
        #             idx2 = len(nums)
        #         else:
        #             idx2 = comb[i]  
        #         # print(nums[idx1:idx2])              
        #         # sub_sum = sum(nums[idx1:idx2])
        #         if idx1 == 0:
        #             sub_sum = dp[idx2-1]
        #         else:
        #             sub_sum = dp[idx2-1] - dp[idx1-1]
        #         max_sub_sum = max(max_sub_sum, sub_sum)
        #     output = min(output, max_sub_sum)
        # return output

        def countGroups(mid):
            temp = 0
            count = 1
            for num in nums:
                temp += num
                if temp > mid:
                    count += 1
                    temp = num # 准备下一组
            return count
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            num_group = countGroups(mid)
            
            if num_group > m: # 划分多了，mid太小了
                left = mid + 1
            else:
                right = mid
        # print(left, mid, right)
        return left # left恰好是满足条件的最少分割，自然就最大
        
        
# @lc code=end

