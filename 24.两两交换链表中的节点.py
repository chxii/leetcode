#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        # res = head.next
        # prev = head
        # curr = head.next
        # end = ListNode(0)
        # while curr:
        #     curr.next, end.next = prev, curr
        #     end = prev
        #     if not prev:
        #         end.next = None
        #         break
        #     prev, curr = prev.next, prev.next.next
        # if not curr:
        #     end.next = prev
        # #     prev.next, curr.next, end.next = curr.next, prev, curr
        # #     if (prev):
        # #         end = prev
        # #         prev, curr = prev.next, prev.next.next 
        # #     else:
        # #         end.next = None
        # #         break
        # # if not curr:
        # #     end.next = prev
        # return res
        if not head or not head.next:
            return head
        end = ListNode(0)    # end初始化为头结点
        res = head.next    # 返回结果首节点   
        pre, cur = head, head.next    # 当前要交换的前节点，后节点
        while cur:
            tmp = cur.next
            end.next = cur    
            cur.next = pre
            end = pre
            if not tmp:    # 节点数为偶数的结束条件
                end.next = None
                break
            pre = tmp
            cur = tmp.next
        if not cur:    # 节点数为奇数的处理
            end.next = pre
        return res

        
# @lc code=end

