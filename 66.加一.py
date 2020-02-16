#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        plus = 1
        for i in range(len(digits)-1, -1, -1):
            curr = digits[i]
            digits[i] = (curr + plus) % 10
            plus = (curr + plus) // 10
        if digits[0] == 0:
            return digits[1:]
        return digits

# @lc code=end

