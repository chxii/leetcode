#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, string: str) -> int:
        if not string:
            return 0
        
        n = len(string)
        idx = 0
        num = ""
        sign = 1
        while idx < n and string[idx] == " ":
            idx += 1
        
        if idx < n and string[idx] == "-":
            sign = -1
            idx += 1
        elif idx < n and string[idx] == "+":
            idx += 1

        while idx < n and string[idx].isdigit():
            num += string[idx]
            idx += 1
        
        if num.isdigit():
            number = int(num)
            if not(number>>31):
                return number * sign
            else:
                if sign == 1:
                    return 2**31 - 1
                else:
                    return -(2**31)
        return 0

## regular expression
# import re
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         INT_MAX = 2147483647    
#         INT_MIN = -2147483648
#         str = str.lstrip()      #清除左边多余的空格
#         num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
#         num = num_re.findall(str)   #查找匹配的内容
#         num = int(*num) #由于返回的是个列表，解包并且转换成整数
#         return max(min(num,INT_MAX),INT_MIN)    #返回值

# @lc code=end

