# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# #方法一
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#             mix_list = []
#             while l1:
#                 mix_list.append(l1.val)
#                 l1 = l1.next
#             while l2:
#                 mix_list.append(l2.val)
#                 l2 = l2.next
#             mix_list.sort()
#             result_link = ListNode(0)
#             q = result_link
#             for i in mix_list:
#                 result_link.next = ListNode(i)
#                 result_link = result_link.next
#             return q.next
#方法一
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        result = cur
        while l1 and l2:
            if l1.val<l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return result.next


l1 = ListNode(1)
l1.next = l11 = ListNode(2)
l11.next = l12 = ListNode(3)
l12.next = l13 = ListNode(4)
l2 = ListNode(1)
l2.next = l21 = ListNode(2)
l21.next = l22 = ListNode(3)
l22.next = l23 = ListNode(4)
s = Solution()
num = s.mergeTwoLists(l1,l2)
while num:
    print(num.val,end="")
    num = num.next