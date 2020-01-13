# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
#递归回溯
class Solution:
    def __init__(self):
        self.visitedHash={}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        #查看该节点是否已经被遍历过，如被遍历直接返回节点
        if head in self.visitedHash:
            return self.visitedHash[head]

        node=Node(head.val, None, None)

        self.visitedHash[head]=node

        node.next=self.copyRandomList(head.next)
        node.random=self.copyRandomList(head.random)

        return node

s = Solution()
node1 = Node(7)
node2 = Node(13,None,node1)
node1.next = node2
node3 = Node(11,None,None)
node2.next = node3
node4 = Node(10,None,None)
node3.next = node4
node5 = Node(1,None,None)
node4.next = node5
node3.random = node5
node4.random = node2

a = s.copyRandomList(node1)
while a:
    print(a.val,end=",")
    a = a.next



