class ArrayQueue:
	def __init__(self, size=100):
		size = size + 1   # +1 is for a reason
		self._arraySize = size
		self._array = [None]*size
		self._rear = 0
		self._front = 0

	def size(self):
		return (self._rear - self._front + self._arraySize) % self._arraySize

	def isEmpty(self):
		return self.size() == 0 #   or   self._front == self._rear

	def isFull(self):    # remainder is used to use array as circular collection
		return self.size() == self._arraySize - 1 #    or return (self._front + self._arraySize + 1) == self._rear + self._arraySize

	def insert(self, val):
		if not self.isFull():
			self._array[self._rear] = val
			self._rear = (self._rear + 1)  % self._arraySize
		else:
			raise RuntimeError("queue full")

	def peek(self):
		if not self.isEmpty():
			return self._array[self._front]
		else:
			raise RuntimeError("queue empty, nothing to return")

	def remove(self):
		val = self.peek()
		self._front = (self._front + 1)  % self._arraySize
		return val


