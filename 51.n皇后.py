#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []

        plane = []
        for _ in range(n):
            row = "".join(["."]*n)
            plane.append(row)

        def isValid(result, level):
            occupied = [0] * n
            positive_diagonal = []
            negative_diagonal = []
            for i in range(level+1):
                for j in range(n):
                    if result[i][j] == 'Q' and occupied[j] == 1:
                        return False
                    # for k in range(1, n):
                    #     if i > k-1 and j > k-1 and result[i-k][j-k] == 'Q' and result[i][j] == 'Q':
                    #         return False
                    #     if i > k-1 and j < n-k and result[i-k][j+k] == 'Q' and result[i][j] == 'Q':
                    #         return False
                    # 如何判断是否在对角上呢
                    # 正对角就是相加之和一样的
                    # 负对角就是相减只差一样的
                    if result[i][j] == 'Q' and (i+j in positive_diagonal or i-j in negative_diagonal):
                        return False
                    if result[i][j] == 'Q':
                        positive_diagonal.append(i+j)
                        negative_diagonal.append(i-j)
                        occupied[j] = 1 
                                   
            return True
                    
        
        def build(level, result, plane):
            if level == n:
                # print(result)                
                output.append(result[:])
                return

            for i in range(n):
                result[level] = result[level][:i] + 'Q' + result[level][i+1:]
                if isValid(result, level):
                    build(level + 1, result, plane)
                result[level] = result[level][:i] + '.' + result[level][i+1:]
        
        build(0, plane, plane)
        return output        
        
# @lc code=end

