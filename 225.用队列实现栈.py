#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l1 = []
        self.l2 = []
        self.size = 0


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.l2) != 0:
            q = self.l2
        else:
            q = self.l1
        q.append(x)
        self.size += 1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.l2) == 0:
            q_empty = self.l2
            q_current = self.l1
        else:
            q_empty = self.l1
            q_current = self.l2
        i = 0
        while i < self.size - 1:
            curr = q_current.pop(0)
            q_empty.append(curr)
            i += 1
        self.size -= 1
        
        return q_current.pop(0)

            


    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.l2) == 0:
            q_empty = self.l2
            q_current = self.l1
        else:
            q_empty = self.l1
            q_current = self.l2
        i, curr = 0, 0
        while i < self.size:
            curr = q_current.pop(0)
            q_empty.append(curr)
            i += 1
        return curr


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

