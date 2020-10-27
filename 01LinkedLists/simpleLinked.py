# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-25,22:25 
# python 3.8.2

# https://blog.csdn.net/qq_42281053/article/details/82225738

# 这个实现不优雅，应该要加上两个哨兵？。


class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None

class Node(object):
    "单链表的节点"
    def __init__(self, item):
        self.elem = item
        self.next = None

class SingleLinkList(object):
    """单链表"""
    # 注意一：默认node节点为空node=None
    def __init__(self, node=None): 
        # 私有属性，内部使用，使用双下划线“__head”
        self.__head = node
 
    def is_empty(self):
        """判断链表是否为空？"""
        return self.__head == None
 
    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            # 注意二：cur是节点Node，cur = cur.next语句将cur.next的内存地址传给了cur
            cur = cur.next 
        return count
 
    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print (cur.elem,)
            cur = cur.next
        print (";")
 
    def add(self, item):
        """在头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node            
 
    def append(self, item):
        """在尾部添加元素，尾插法"""
        # 注意三：node = Node(item)、cur.next = node
        node = Node(item)
        if self.__head == None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
 
    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """        
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            count = 0
            cur = self.__head
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node
 
    def remove(self, item):
        """删除节点"""        
        cur = self.__head        
        pre = None
        while cur != None:
            if cur.elem == item:
                if pre == None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next                
 
    # # C++? Good code 
    # remove_list_entry(entry)
    # {
    #     // The *indirect* pointer points to the
    #     // *address* of the thing we'll update
    #     indirect = &head;

    #     // Walk the list, looking for the thing that
    #     // points to the entry we wants to remove
    #     while ((*indirect) != entry)
    #         indirect = &(*indirect)-> next;

    #     // .. adn just remove it
    #     *indirect = entry->next;
    # }

    # bad code
    # remove_list_entry(entry)
    # {
    #     prev = NULL;
    #     walk = head;

    #     // Walk the list
    #     while (walk != entry){
    #         prev = walk;
    #         walk = walk->next;
    #     }

    #     // Remove the entry by updating the
    #     // head or the previous entry

    #     if (!prev)
    #         head = entry->next;
    #     else
    #         prev->next = entry->next;
    # }

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head         
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
 
if __name__ == '__main__':
    li = SingleLinkList()
    print(li)
    print ("Is this List empty ?  : %s" %(li.is_empty()))
    print (li.length())
    li.append(56)
    li.append(78)
    li.add(34)
    li.add(12)
    li.insert(2, 90)
    print ("Is this List empty ?  : %s" %(li.is_empty()))
    print (li.length())
    li.travel()
    print (li.search(78))
    li.remove(90)
    li.travel()
