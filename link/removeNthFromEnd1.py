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
        cur = head
        while n > 0 and cur:
            cur = cur.next
            n -= 1
        #说明n = lens
        if n==0 and cur == None:
            return head.next
        # 说明n>链表长度
        if n >=0 and cur == None:
            return head
        slow = head
        while cur.next:
            slow = slow.next
            cur = cur.next
        slow.next = slow.next.next
        return head

l1 = ListNode(1)
l1.next = l11 = ListNode(2)
l11.next = l12 = ListNode(3)
l12.next = l13 = ListNode(4)
s = Solution()
num = s.removeNthFromEnd(l1,1)
while num:
    print(num.val,end="")
    num = num.next