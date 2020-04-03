#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        getlen = map(len, strs)
        shortest_len = min(getlen)
        ans = ""
        for l in range(1, shortest_len+1):
            pre = strs[0][:l]
            flag = 0
            for i in range(1, len(strs)):
                if strs[i][:l] != pre:
                    flag = 1
                    break
            if flag == 0:
                ans = pre
        return ans


        
        # i = 0
        # while True:
        #     ans = strs[0][i]
        #     for j in range(1, len(strs)):
        #         if ans == strs[i][j]:
        #             continue
        #         else:


# @lc code=end

