from pythonds.basic.queue import Queue 

class Queue:

	def __init__(self):
		self.items = []

		def isEmpty(self):
			if len(self.items) == 0:
				return True
			else:
				return False
			# OR
			if size(self) == 0:
				return True
			else: 
				return False

		def enqueue(self, item):
			self.items.extend(item)
			#
			self.items.insert(0, item)

		def dequeue(self):
			item = self.items[0]
			del self.items[0]
			return item
			#
			return self.items(pop)

		def size(self):
			return len(self.items)