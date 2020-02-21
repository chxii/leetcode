#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.dfs(1, k, n, [], res)
        return res

    def dfs(self, start, k, n, pre, res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # 在第 k 层结算
        if len(pre) == k:
            res.append(pre[:])
            return

        # （原版）
        # for i in range(start, n + 1):
        #     pre.append(i)
        #     self.dfs(i + 1, k, n, pre, res)
            
        #     # 回溯的时候，状态重置
        #     pre.pop()

        # 注意：这里 i 的上限是归纳得到的 (优化)
        for i in range(start, n - (k - len(pre)) + 2):
            pre.append(i)
            self.dfs(i + 1, k, n, pre, res)
            pre.pop()


# @lc code=end

