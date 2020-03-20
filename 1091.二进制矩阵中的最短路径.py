#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start

# BFS可通过版本！
# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1:
#             return -1
#         elif n <= 2:
#             return n
#         queue = [(0, 0, 1)]
#         grid[0][0] = 1
#         while queue:
#             i, j, step = queue.pop(0)           
#             for dx, dy in [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]:
#                 if i+dx == n-1 and j+dy == n-1:
#                     return step + 1
#                 if 0 <= i+dx < n and 0 <= j+dy < n and grid[i+dx][j+dy] == 0:
#                     queue.append((i+dx, j+dy, step+1))
#                     grid[i+dx][j+dy] = 1                    
#         return -1


## 尝试A* 版本
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:       
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        elif n <= 2:
            return n

        def heuristic(x, y):
            return max(abs(n-1 - x), abs(n-1 - y))
        
        h = []
        heapq.heappush(h,(0, (0, 0, 1)))
        visited = set()
        while h:
            _, (i, j, step) = heapq.heappop(h)

            if (i, j) in visited:
                continue
            visited.add((i, j))

            for dx, dy in [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]:
                next_i, next_j = i+dx, j+dy

                if next_i == n - 1 and next_j == n - 1:
                    return step + 1

                if 0 <= next_i < n and 0 <= next_j < n and grid[next_i][next_j] == 0:
                    heapq.heappush(h, (step + heuristic(next_i, next_j), (next_i, next_j, step+1)))
                          
        return -1

# @lc code=end

