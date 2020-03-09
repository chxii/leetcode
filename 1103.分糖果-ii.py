#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output = [0] * num_people
        curr = 1
        idx = 0
        while candies > 0:
            output[idx] += min(curr, candies)
            candies -= min(curr, candies)
            # print(candies)
            curr += 1
            idx = (idx + 1) % num_people
        return output
        
# @lc code=end

