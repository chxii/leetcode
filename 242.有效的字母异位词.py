#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp = {}
        for i in s:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
        for j in t:
            if j not in tmp:
                return False
            else:
                tmp[j] -= 1
        for d in tmp:
            if tmp[d] != 0:
                return False
        return True

        ## 排序的解法：
        # return len(s) == len(t) and sorted(s) == sorted(t)
                
        
# @lc code=end

