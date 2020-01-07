#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class listNode(object):
    def __init__(self,x):
        self.elem = x
        self.next = None

class link_add(object):
    def solution(self,l1,l2):
        res = pre = listNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.elem
                l1 = l1.next
            if l2:
                carry += l2.elem
                l2 = l2.next
            carry,val = divmod(carry,10)
            pre.next = listNode(val)
            pre = pre.next
        return res.next
if __name__ == '__main__':
    l1 = listNode(1)
    l1.next = l11 = listNode(2)
    l11.next = l12 = listNode(2)
    l2 = listNode(1)
    l2.next = l21 = listNode(2)
    l21.next = l22 = listNode(2)
    sl = link_add()
    res = sl.solution(l1,l2)
    while res:
        print(res.elem,end="")
        res = res.next


