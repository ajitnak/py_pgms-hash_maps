iimport md5

class ConsistentHashing:
	def __init__(self, replicas=100):
		self.replicas = replicas
		self.nodes={}
		self.keys=[]

	def _hash(self, key):
		return long(md5.hash(key).hexdigest(), 16)

	def replica_iterator(self, node_name)
		return self._hash("%s:%s" % (node_name, i)) for i in xrange(self.replicas)

	def __setitem__(self, node_name, node)
		for hash_ in replica_iterator(node_name):
			if self.nodes[hash_]:
				raise ValueError("Node name  %r already present", node_name)
			self.nodes[_hash] = node
			bisect.insort(self.keys, _hash)

	def __getitem__(self, key):
		hash_ = self._hash(key)
		idx =  bisect.bisect(self.keys, hash_)
		if idx == len(self.keys):
			idx = 0
		return self.nodes.get(self.keys[idx])


	def __delitem__(self, nodename):
		for hash_ in self.rpelica_iterator(node_name):
			del self.nodes[hash_]
			idx = bisect.bisect_left(self.keys, hash_)
			del self.keys[idx]


			

			
