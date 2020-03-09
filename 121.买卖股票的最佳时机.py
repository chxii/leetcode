#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        output = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price > min_price:
                output = max(output, price - min_price)
        return output
# @lc code=end

