#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n1 = len(set(s))
        n2 = len(set(t))
        if n1 != n2:
            return False
        d = {}
        n = len(s)
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                print(d[s[i]], t[i])
                if d[s[i]] != t[i]:
                    return False
        return True

# @lc code=end

