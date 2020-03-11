#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        amount = sum(A)
        single = amount / 3
        if single % 1 == 0: 
            s = 0
            l = []
            for i in range(len(A)):
                s += A[i]
                if s == single:
                    l.append(s)  # 第一段求出后,加入数组,和清零
                    s = 0 
                    if len(l) == 2 and i != len(A)-1: # 求出前两部分和后,求第三部分     超出索引求和为0,我也不知道
                        c = sum(A[i+1:])
                        l.append(c)
                        return l[1] == l[0] == l[2]
        return False

        
# @lc code=end

