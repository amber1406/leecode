#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        if head == None or n == 0:
            return head
        lens=0
        cur = head
        pre = None
        while cur:
            lens+=1
            cur = cur.next
        if lens == n:
            return head.next
        pos=0
        cur = head
        while pos < lens - n:
            pre = cur
            cur = cur.next
            pos += 1
        pre.next = cur.next
        return head

l1 = ListNode(1)
l1.next = l11 = ListNode(2)
l11.next = l12 = ListNode(3)
l12.next = l13 = ListNode(4)
s = Solution()
num = s.removeNthFromEnd(l1,3)
while num:
    print(num.val,end="")
    num = num.next