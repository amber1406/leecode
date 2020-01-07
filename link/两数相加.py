#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry=0
        res=pre=ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            carry, val=divmod(carry, 10)
            # pre.next=pre=ListNode(val)
            pre.next = ListNode(val)
            pre = pre.next
            # pre = pre.next
        return res.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(243)
    l2 = ListNode(567)
    num = s.addTwoNumbers(l1,l2)
    while num:
        print(num.val,end="")
        num = num.next


