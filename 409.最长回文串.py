#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        c = collections.Counter(s)
        count = 0
        left = 0
        for key in c:
            count += c[key] // 2 * 2
            if c[key] % 2 != 0 and left == 0:
                left = 1
        if left == 1:
            count += 1
        return count
        
# @lc code=end

