#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv", "9": "wxyz"}
        output = []
        def recur(digits, res):
            if len(digits) == 0:
                output.append(res)
                return
            for i in d.get(digits[0]):
                recur(digits[1:], res + i)
        recur(digits, "")
        return output
        
        
# @lc code=end

