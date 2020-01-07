# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # #迭代
        # cur=head
        # nexts=head.next
        # cur.next=None
        # while nexts:
        #     temp=nexts.next
        #     nexts.next=cur
        #     cur=nexts
        #     nexts=temp
        # return cur
        # #递归
        last_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return  last_head

l1 = ListNode(1)
l1.next = l11 = ListNode(2)
l11.next = l12 = ListNode(3)
l12.next = l13 = ListNode(4)
s = Solution()
num = s.reverseList(l1)
while num:
    print(num.val,end="")
    num = num.next


