#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        state = [board[i][j] for i in range(2) for j in range(3)]
        if state == [1, 2, 3, 4, 5, 0]:
            return 0
        idx_dict = {0: [1, 3], 
                      1: [0, 2, 4],
                      2: [1, 5], 
                      3: [0, 4],
                      4: [1, 3, 5],
                      5: [2, 4]}
        queue = [(state, 1)]
        visited = []
        while queue:
            state, step = queue.pop(0)
            zero_index = state.index(0)
            for idx in idx_dict.get(zero_index):
                new_state = state[:]
                new_state[zero_index], new_state[idx] = new_state[idx], new_state[zero_index]
                # print(new_state, state, step)
                if new_state == [1, 2, 3, 4, 5, 0]:
                    return step
                if new_state not in visited:
                    queue.append((new_state, step + 1))
                    visited.append(new_state)

        return -1
        
# @lc code=end

