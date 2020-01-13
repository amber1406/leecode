#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # if not head:
        #     return True
        # ls=[]
        # cur=head
        # while cur:
        #     ls.append(cur.val)
        #     cur=cur.next
        # return ls == ls[::-1]
        #判断为空或者长度为1
        if not head or not head.next:
            return True
        slow = head
        fast = head
        q = slow
        #采用快慢指针
        while fast and fast.next:
            slow = slow.next
            fast =fast.next.next
        revers_list = self.reverse_list(slow) #反转链表后半部分
        while revers_list:
            if revers_list.val != q.val:
                return False
            revers_list = revers_list.next
            q = q.next
        return True
    #反转后边的数
    def reverse_list(self,head):
        if not head.next:
            return head
        last_head = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return last_head

l1 = ListNode(1)
l1.next = l11 = ListNode(1)
# l11.next = l12 = ListNode(1)
# l12.next = l13 = ListNode(2)
s = Solution()
num = s.isPalindrome(l1)
print(num)
