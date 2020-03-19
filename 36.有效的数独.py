#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row = len(board)
        # col = len(board[0])
        for i in range(9):
            d = collections.Counter(board[i])

            for key in d:
                if key != "." and d[key] > 1:
                    return False
        
        for j in range(9):
            d = collections.Counter()
            for i in range(9):
                d[board[i][j]] += 1

            for key in d:
                if key != "." and d[key] > 1:
                    return False
        
        for i in range(3):
            for j in range(3):
                d = collections.Counter()
                for xi in range((i+1)*3-3, (i+1)*3):
                    for xj in range((j+1)*3 -3, (j+1)*3):
                        # print(xi, xj)
                        d[board[xi][xj]] += 1

                for key in d:
                    if key != "." and d[key] > 1:
                        return False
        
        return True
                
        
# @lc code=end

