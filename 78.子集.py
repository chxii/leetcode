#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        def recur(i, res):
            output.append(res)
            for j in range(i,n):
                recur(j + 1, res + [nums[j]])
        recur(0, [])
        return output
        
# @lc code=end

