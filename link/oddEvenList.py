# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        odd_head = odd = head.next
        while cur.next and odd.next:
            cur.next = odd.next
            cur = cur.next
            odd.next = cur.next
            odd = odd.next
        cur.next = odd_head
        return head
l1 = ListNode(1)
l1.next = l11 = ListNode(2)
l11.next = l12 = ListNode(3)
l12.next = l13 = ListNode(4)
s = Solution()
num = s.oddEvenList(l1)
while num:
    print(num.val,end="")
    num = num.next