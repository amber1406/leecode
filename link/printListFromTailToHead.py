#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# #方法一简单列表保存输出
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         # write code here
#         new_list = []
#         while listNode:
#             new_list.append(listNode)
#             listNode = listNode.next
#         return [i.val for i in new_list[::-1]]

#递归
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res = []
        def printNode(listNode):
            if listNode:
                printNode(listNode.next)
                res.append(listNode.val)
        printNode(listNode)
        return res

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = l1.next = ListNode(2)
    l3 = l2.next = ListNode(3)
    s= Solution()
    print(s.printListFromTailToHead(l1))
