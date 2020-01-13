#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
       self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            # print(cur_node.elem)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度优先"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=",")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_oder(self,node):
        """深度优先之前序遍历"""
        while node is None:
            return
        print(node.elem,end=",")
        self.pre_oder(node.lchild)
        self.pre_oder(node.rchild)

    def mid_oder(self,node):
        """深度优先之前序遍历"""
        if node is None:
            return
        self.mid_oder(node.lchild)
        print(node.elem,end=",")
        self.mid_oder(node.rchild)

    def last_oder(self,node):
        """深度优先之前序遍历"""
        while node is None:
            return
        self.last_oder(node.lchild)
        self.last_oder(node.rchild)
        print(node.elem,end=",")


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.pre_oder(tree.root)
    print(" ")
    tree.mid_oder(tree.root)
    print(" ")
    tree.last_oder(tree.root)
