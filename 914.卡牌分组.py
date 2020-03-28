#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
import collections
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # c = collections.Counter(deck)       

        # flag = 0
        # for key in c:
        #     v = c[key]
        #     if v < 2:
        #         return False
        #     if flag == 0:
        #         value = v
        #         flag = 1

        #     if math.gcd(v, value) < 2:
        #         return False 

        #     value = math.gcd(v, value)           
        # return True

        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2

# @lc code=end

