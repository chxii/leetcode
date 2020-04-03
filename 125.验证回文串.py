#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while not (s[i].isalpha() or s[i].isnumeric()) and i < j:
                i += 1
            while not (s[j].isalpha() or s[j].isnumeric()) and i < j:
                j -= 1
            # print(i, j, s[i], s[j])
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True

# @lc code=end

