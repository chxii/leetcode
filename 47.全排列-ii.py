#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def per(nums, result):
            if len(nums) == 0:
                if result not in output:
                    output.append(result[:])
                return
            
            for i in range(len(nums)):
                result.append(nums[i])
                per(nums[:i] + nums[i+1:], result)
                result.pop()
                
        per(nums, [])
        return output
# @lc code=end

