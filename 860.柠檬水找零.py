#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        curr5 = 0
        curr10 = 0

        for bill in bills:
            if bill == 5:
                curr5 += 1
            elif bill == 10:
                if curr5 >= 1:
                    curr5 -= 1
                else:
                    return False
                curr10 += 1
            else: # bill == 20
                if curr10 >= 1 and curr5 >= 1:
                    curr10 -= 1
                    curr5 -= 1
                elif curr5 >= 3:
                    curr5 -= 3
                else:
                    return False
        
        return True
                

        
# @lc code=end

