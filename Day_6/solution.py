from collections import OrderedDict

class LRUCache:
	def __init__(self, capacity):
		super().__init__()
		self.capacity = capacity
		self.cache = OrderedDict()

	def put(self,key,value):
		if key not in self.cache.keys():
			if len(self.cache) >= self.capacity:
				self.cache.popitem(last = False)
		self.cache[key] = value
	
	def get(self, key):
		if key in self.cache:
			self.cache.move_to_end(key)
			return self.cache[key]
		else:
			return -1

	def get_cache(self):
		return self.cache
