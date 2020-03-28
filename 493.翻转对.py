#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def helper(nums, left, right):
            if right == left:
                return 0
            mid = left + 1 + (right-left)//2
            
            ans = helper(nums, left, mid-1) + helper(nums, mid, right)
            nums[left:mid] = sorted(nums[left:mid])
            nums[mid:right+1] = sorted(nums[mid:right+1])
            i, j = left, mid
            while i < mid and j <= right:
                if nums[i] > 2*nums[j]:  
                    ans += mid - i
                    j += 1
                else:
                    i += 1
            return ans
        
        if not nums:
            return 0

        return helper(nums, 0, len(nums)-1)

# @lc code=end

