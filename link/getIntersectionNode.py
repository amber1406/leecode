#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        curB = headB
        if not curA or not curB:
            return None
        dic = dict()
        while curA:
            dic[curA] = 1
            curA = curA.next
        while curB:
            if dic.get(curB):
                return curB
            curB = curB.next