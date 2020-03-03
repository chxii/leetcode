#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s or len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     return 1
        
        # d = {}
        # count = 0
        # subCount = 1

        # i = 0
        # j = 1
        # d[s[i]] = 1
        # while i < len(s) and j < len(s):
        #     if s[j] in d:
        #         i += 1
        #         j = i + 1
        #         d = {}
        #         count = max(count, subCount)
        #         d[s[i]] = 1
        #         subCount = 1
        #     else:
        #         d[s[j]] = 1
        #         j += 1
        #         subCount += 1
        
        # return max(count, subCount)

        # sliding window solution
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len
        

# @lc code=end

