# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=head
        fast=head
        while True:
            if not (fast and fast.next):
                return
            slow=slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while slow != fast:
            fast=fast.next
            slow=slow.next
        return fast
