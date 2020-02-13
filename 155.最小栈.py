#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = None
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if (self.minVal == None):
            self.minVal = x
        else:
            self.minVal = min(self.minVal, x)
        

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) > 0:
            self.minVal = min(self.stack)
        else:
            self.minVal = None

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

