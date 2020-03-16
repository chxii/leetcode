#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        x = len(grid)
        y = len(grid[0])
        count = 0
        max_area = 0

        def find(a, b):
            q = [(a,b)]
            area = 0
            while q:
                i, j = q.pop(0)
                area += 1
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 0
                    q.append((i-1, j))
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 0
                    q.append((i, j-1))
                if j+1 < y and grid[i][j+1] == 1:
                    grid[i][j+1] = 0
                    q.append((i, j+1))
                if i+1 < x and grid[i+1][j] == 1:
                    grid[i+1][j] = 0
                    q.append((i+1, j))
            return area

        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    count += 1
                    max_area = max(find(i, j), max_area)
        # print(count, max_area)
        return count if count == 0 else max_area    
        
# @lc code=end

