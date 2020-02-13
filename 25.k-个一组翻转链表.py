#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        out = dummy # for output
        
        while True:
            stack = []
            count = k
            curr = head
            
            while count > 0 and curr:
                stack.append(curr)
                curr = curr.next
                count -= 1
            
            # 剩下的不够k个：正常顺序
            if count > 0: 
                dummy.next = head
                break

            while stack:
                dummy.next = stack.pop()
                dummy = dummy.next
            
            # dummy.next = curr
            head = curr
            

        return out.next
            

        
# @lc code=end

