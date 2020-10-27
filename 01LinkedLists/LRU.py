# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-10-25,20:06
# python 3.8.3

# lru

class Node():
    def __init__(self, key, val, prev=None, succ=None) -> None:
        self.key = key
        self.val = val
        # 前驱
        self.prev = prev
        # 后继
        self.succ = succ

    def __repr__(self) -> str:
        return str(self.val)


class LinkedList():
    '''
    Header, Tail 只是一个"哨兵/占位符"，并不会直接存数据
    越靠近tail代表数据越新
    '''
    def __init__(self) -> None:
        self.head = Node(None, 'header')
        self.tail = Node(None, 'tail')
        # Header <--> Tail
        self.head.succ = self.tail
        self.tail.prev = self.head

    def length(self):
        """
        LRU中没有用到，
        """
        node = self.head
        count = 0
        while node.succ != self.tail:
            count += 1
            node = node.succ 
        return count 

    def is_empty(self):
        """
        LRU中没有用到，
        """
        return self.head.succ == self.tail 

    def append(self, node):
        '''
        将node节点添加到链表尾部
        '''
        # 保存最后一个节点(tail不算最后一个节点)
        prev = self.tail.prev
        # prev <--> node <--> prev.succ，可以调用self.insert(node, prev)
        prev.succ = node
        node.prev = prev
        node.succ = prev.succ
        node.succ.prev = node
    
    # 在LRU中没有用到
    def insert(self, node, prev):
        succ = prev.succ
        # prev <--> node <--> succ
        prev.succ = node
        node.prev = prev
        node.succ = succ
        succ.prev = node


    def delete(self, node):
        '''
        删除节点
        '''
        # prev <--> node <--> succ
        prev = node.prev
        succ = node.succ
        # prev <--> succ
        succ.prev, prev.succ = prev, succ

    def get_haad(self):
        # 返回第一个节点(head不算第一个节点)
        return self.head.succ


class LRU:
    def __init__(self, cap=100):
        """
        使用hashMap(python字典)和链表实现
        """
        # cap即capacity, 容量
        self.cap = cap
        self.cache = {}   # {key: Node}
        self.linked_list = LinkedList()

    def get(self, key):
        if key not in self.cache:
            return None

        self.put_recently(key)
        return self.cache[key]

    def put_recently(self, key):
        # 把节点更新到链表尾部
        node = self.cache[key]
        self.linked_list.delete(node)
        self.linked_list.append(node)

    def put(self, key, value):
        # 能查到的话先删除原数据再更新(COW?)
        if key in self.cache:
            self.linked_list.delete(self.cache[key])
            # 必须要用key,val构建一个新的node，因为之前的node的val可能已经改变了。
            self.cache[key] = Node(key, value)
            self.linked_list.append(self.cache[key])
            return

        if len(self.cache) >= self.cap:
            # 容量满了，删除最旧的最点
            node = self.linked_list.get_head()
            # 需要把hashMap及链表中node节点都删除了。
            self.linked_list.delete(node)
            del self.cache[node.key]

        # 将新数据加到lru的尾部(即：最近使用)
        u = Node(key, value)
        self.linked_list.append(u)
        self.cache[key] = u