#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for word in s.split():
            ans.append(word[::-1])
        return " ".join(ans)
        
# @lc code=end

