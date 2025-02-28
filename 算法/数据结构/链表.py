class Node:
    def __int__(self,item):
        self.item = item
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

#创建链表
# 头插法
def print_linklist(lk):
    while lk:
        print(lk.item,end=",")
        lk = lk.next

def create_linklist(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

#尾插法
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

