class ArrayStack:
    def __init__(self, size):
        self.size = size
        # if nd != 1:
        #     self.array = [[None for j in range(size / nd)] for i in range(nd)]
        # else:
        self.array = [None] * size
        self.populated = 0
        self.front = self.rear = 0

    def isEmpty(self):
        return self.populated == 0

    def isFull(self):
        return self.rear == self.size-1

    def push(self, val):
        if self.isFull():
            return 'Array memory has been exceeded'
        else:
            self.array[self.rear] = val
            self.rear += 1
        self.populated += 1

    # def insert(self, val, index):
    #     if not self.isFull():
    #         for i in range(self.rear, index-1, -1):
    #             self.array[i+1] = self.array[i]
    #         self.array[index] = val
    #         self.populated += 1
    #     else:
    #         return 'Array memory has been exceeded'

    # def remove(self, val):
    #     if not self.isEmpty():
    #         index = 0
    #         while self.array[index] != val:
    #             index += 1
    #         for i in range(index, self.size):
    #             self.array[i] = self.array[i+1]
    #         self.populated -= 1
    #     else:
    #         return 'Empty Error'

    def pop(self):
        data = self.array[self.rear-1]
        self.array[self.rear-1] = None
        self.populated -= 1
        self.rear -= 1
        return data

    def __str__(self):
        s = ''
        # for i in range(self.dimension):
        for element in self.array:
            if element is None:
                break
            s += str(element) + '\t'
        return s

    def __len__(self):
        return self.populated
