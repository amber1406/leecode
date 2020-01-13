# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
#迭代法
class Solution:
    def __init__(self):
        self.visitedHash={}

    def getCloneNode(self,node):
        if node:
            if node in self.visitedHash:
                return self.visitedHash[node]
            else:
                self.visitedHash[node] = node
                return self.visitedHash[node]
        return None

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        old_node = head
        new_node = Node(old_node.val,None,None)
        self.visitedHash[old_node] = new_node

        while old_node:
            new_node.random = self.getCloneNode(old_node.random)
            new_node.next = self.getCloneNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return self.visitedHash[head]


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



