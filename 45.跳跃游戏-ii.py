#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1

        i = 0
        output = 0
        while i < len(nums) - 1:
            current_steps = nums[i]
            if current_steps == 1:
                max_step = 1
            else:
                max_step = 0
                max_val = 0
                for j in range(1, current_steps+1):
                    if i + j < len(nums):
                        if nums[i+j] > max_val:
                            max_val = nums[i+j]
                            max_step = j
            # print(i, max_step)
            i += max_step
            output += 1
        
        return output        
            
# @lc code=end

