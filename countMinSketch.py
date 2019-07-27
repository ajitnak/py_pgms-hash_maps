import mmh3

class CountMinSketch():
	def __init__(self, width, depth, seeds):
		self.depth = depth # num hash functions
		self.width = width
		self.table = [[0]*width for i in xrange(depth)]
		self.seeds = seeds

	def increment(self, key):
		for i in xrange(self.depth):
			idx = mmh3.hash(key, i+1) % self.width
			self.table[i][idx] += 1

	def estimate(self, key):
		min_est = self.width
		for i in xrange(self.depth):
			idx = mmh3.hash(key, i+1) % self.width
			if self.table[i][idx] < min_est:
				min_est = self.table[i][idx] 
		return min_est

			
			
		
			
			
		

		
