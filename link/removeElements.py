#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        cur = ListNode(0)
        cur.next = head
        p = cur
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return cur.next

l1 = ListNode(1)
l1.next = l11 = ListNode(2)
l11.next = l12 = ListNode(3)
l12.next = l13 = ListNode(4)
s = Solution()
num = s.removeElements(l1,1)
while num:
    print(num.val,end="")
    num = num.next