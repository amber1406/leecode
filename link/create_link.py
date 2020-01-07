#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Nodelist(object):
    def __init__(self, item=None):
        self.val=item
        self.next=None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__head=None
        self.length=0

    def isEmpty(self):
        return self.__head == None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        count=0
        cur=self.__head
        if index < 0 or self.length <= index:
            return -1
        while cur:
            if count == index:
                return cur.val
            count+=1
            cur=cur.next

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node=Nodelist(val)
        node.next=self.__head
        self.__head=node
        self.length+=1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node=Nodelist(val)
        cur=self.__head
        while cur.next:
            cur=cur.next
        cur.next=node
        self.length+=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node=Nodelist(val)
        cur=self.__head
        pre=None
        count=0
        if index < 0 or index > self.length:
            return -1
        elif index == 0:
            self.__head=node
            node.next=cur
        else:
            while cur:
                pre=cur
                cur=cur.next
                count+=1
                if count == index:
                    pre.next=node
                    node.next=cur
        self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur=self.__head
        pre=None
        count=0
        if index < 0 or index >= self.length:
            return -1
        elif index == 0:
            self.__head=cur.next
        else:
            if self.length == 1:
                self.__head=None
            else:
                while cur:
                    pre=cur
                    cur=cur.next
                    count+=1
                    if count == index:
                        pre.next=cur.next
        self.length-=1

    def travel(self):
        cur=self.__head
        while cur.next:
            print(cur.val, end="")
            cur=cur.next


linkedList=MyLinkedList()
linkedList.addAtHead(2)
print(linkedList.get(1))
linkedList.addAtHead(2)
linkedList.addAtHead(7)
linkedList.addAtHead(3)
linkedList.addAtHead(2)
linkedList.addAtHead(5)
linkedList.addAtTail(5)  # 链表变为1-> 2-> 3
print(linkedList.get(5))  # 链表变为1-> 2-> 3
linkedList.deleteAtIndex(6)  # 链表变为1-> 2-> 3
linkedList.deleteAtIndex(4)  # 链表变为1-> 2-> 3

# print(linkedList.get(4))       #返回2
# linkedList.deleteAtIndex(5)  #现在链表是1-> 3
# print(linkedList.get(3))       #返回2
# # linkedList.addAtHead(4)
# # linkedList.addAtIndex(5,0)  #现在链表是1-> 3
# # linkedList.addAtHead(6)
# # print(linkedList.get(2))
