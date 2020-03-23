#
# @lc app=leetcode.cn id=945 lang=python3
#
# [945] 使数组唯一的最小增量
#

# @lc code=start
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # 贪心算法
        A.sort()
        count = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                count += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        return count
# @lc code=end

