#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {}
        for stone in stones:
            d[stone] = set()
        
        d[0].add(0)
        for stone in stones:
            for k in d[stone]:
                for step in range(k-1, k+2):
                    if step > 0 and stone+step in d:
                        d[stone+step].add(step)
        # print(d)
        return len(d.get(stones[-1])) > 0          
        
# @lc code=end

