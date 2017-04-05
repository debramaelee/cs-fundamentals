# new() - creates new stack
# push() - adds an object onto the stack
# pop() - removes the top item from the stack
# top() - returns the top item from the stack without removing it
# peek() - returns an item at the top of the stack
# size() - returns number o fobjects in stack
# isEmpty() - indicates whether stack is empty or not


class myStack(object):

	def __init__(self):
		self.data = []

	def push(self, item):
		self.data.append(item)

	def pop(self):
		item = self.data[len(self.data) - 1]
		del self.data[len(self.data) - 1]
		return item

	def peek(self):
		return self.data[len(self.data) - 1]

	def size(self):
		return len(self.data)

	def isEmpty(self):
		if len(self.data) == 0: 
			return True
		else:
			return False
		# more efficient method
		if size(self) === 0:
			return True
		else: 
			return False
