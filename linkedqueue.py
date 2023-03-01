class Node:
    def __init__(self, data, val=None):
        self.data = data
        self.next = val


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def peak(self):
        return self.front.data

    def count(self):
        return self.count

    def Enqueue(self, val):
        node = Node(val)
        if self.isEmpty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.count += 1

    def Dequeue(self):
        if self.isEmpty():
            raise 'Queue is Empty'
        tmp = self.front
        self.front = tmp.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return tmp.data


if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    q.Enqueue(10)
    q.Enqueue(11)
    q.Enqueue(20)
    q.Enqueue(13)
    print(q.peak())
    print(q.Dequeue())
    print(q.peak())
