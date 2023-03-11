class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def AddFront(self, val):
        node = Node(val)
        if not self.isEmpty():
            tmp = self.head
            self.head = node
            self.head.next = tmp
            self.head.next.prev = self.head
        else:
            self.head = node
        self.count += 1

    def AddAfter(self, val, node):
        nod = Node(val)
        if not self.isEmpty():
            tmp = self.head
            while tmp.data != node:
                tmp = tmp.next
            tmp1 = tmp.next
            tmp.next = nod
            nod.prev = tmp
            if tmp1 is not None:
                nod.next = tmp1
                tmp1.prev = nod
        else:
            raise 'Nodeset is empty'
        self.count += 1

    def AddBack(self, val, node):
        if not self.isEmpty():
            tmp = self.head
            while tmp.next.data != node:
                tmp = tmp.next
            self.AddAfter(val, tmp.data)
        else:
            raise 'Node is empty'

    def append(self, val):
        node = Node(val)
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = node

    def remove(self, val):
        tmp = self.head
        # Front Node
        if self.head.data == val:
            self.head = self.head.next
            self.count -= 1
            return
        # In Between
        while tmp.next.data != val:
            tmp = tmp.next
        if tmp.next.next is not None:
            tmp.next = tmp.next.next
            tmp.next.next.prev = tmp
        else:
            # Last Node
            tmp.next = None
        self.count -= 1

    def __str__(self):
        tmp = self.head
        s = ''
        while tmp.next is not None:
            s += f'{tmp.data}\t'
            tmp = tmp.next
        s += f'{tmp.data}'
        return s


if __name__ == '__main__':
    linkedlist = DoubleLinkedList()
    linkedlist.AddFront(10)
    linkedlist.AddFront(20)
    print(linkedlist)
    linkedlist.AddAfter(30, 10)
    linkedlist.AddAfter(50, 20)
    print(linkedlist)
    linkedlist.AddBack(15, 50)
    linkedlist.AddBack(35, 30)
    print(linkedlist)
    linkedlist.remove(10)
    print(linkedlist)
    linkedlist.remove(30)
    print(linkedlist)
    linkedlist.remove(20)
    print(linkedlist)
    linkedlist.append(45)
    print(linkedlist)
