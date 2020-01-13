
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

#迭代法
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        pre_node=Node(0, None, head, None)
        prev=pre_node

        stack=[]
        stack.append(head)

        while stack:
            cur=stack.pop()

            prev.next=cur
            cur.prev=prev

            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child=None
            prev=cur
        pre_node.next.prev=None
        return pre_node.next

# 递归深度优先搜索
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # 递归深度优先
        if not head:
            return head
        pre_node=Node(0, None, head, None)
        self.flatten_dfs(pre_node, head)
        pre_node.next.prev=None
        return pre_node.next

    def flatten_dfs(self, pre_node, cur_node):
        if not cur_node:
            return pre_node

        cur_node.prev=pre_node
        pre_node.next=cur_node

        temp_next=cur_node.next
        tail=self.flatten_dfs(cur_node, cur_node.child)
        cur_node.child=None
        return self.flatten_dfs(tail, temp_next)





