#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        #print(dp)
        return dp[-1][-1]

# 如果S的第jj个字符和T的第ii个字符相同，即S[j] == T[i]。这时如果想让S的前jj个字符中的某ii个字符和T的前ii个字符匹配，有两种方式：
# 匹配时包含S的第jj个字符，这时dp[i][j] = dp[i-1][j-1]。
# 匹配时不包含S的第jj个字符，这时dp[i][j] = dp[i][j-1]。
# 因此，这种情况下的动态方程为dp[i][j] = dp[i-1][j-1] + dp[i][j-1]。
# 如果S的第jj个字符和T的第ii个字符不相同，即S[j] != T[i]。这时如果想让S的前jj个字符中的某ii个字符和T的前ii个字符匹配，相当于让S的前j-1j−1个字符中的某ii个字符和T的前ii个字符匹配，即dp[i][j] = dp[i][j-1]。



# @lc code=end

