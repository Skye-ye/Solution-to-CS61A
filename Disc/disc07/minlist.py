class MinList:
	def __init__(self):
		self.items = []
		self.size = 0

	def append(self, item):
		self.items.append(item)
		self.size += 1

	def pop(self):
		min_item = min(self.items)
		self.items.remove(min_item)
		self.size -= 1
		return min_item

	def size(self):
		return self.size
		