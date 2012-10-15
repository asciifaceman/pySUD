#
#
#
'''
A -> B
B -> C
B -> D
B -> E
C -> B
D -> B
E -> B
'''

graph = {'Birth Spring': ['B'],
	'B': ['C', 'D', 'E'],
	'C': ['B'],
	'D': ['B'],
	'E': ['B']}
	
def find_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		print "no need"
		return path
	if not graph.has_key(start):
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath: return newpath
	return None
int1 = 0
int2 = 0
int3 = 0
class Player(object):
	trav = 0
	def __init__(self):
		self.location = 'Birth Spring'
	def where(self):
		print "Currently in %s" % self.location
	'''def go(self, graph, start, end, path=[]):
		global int3
		int3 += 1
		print int3
		path = path + [start]
		if start == end:
			print "You're there!"
			self.location = end
			return path
		if not graph.has_key(start):
			print "graph has key"
			return None
		for node in graph[start]:
			global int1 
			int1 += 1
			print "for iter: %s" % int1
			if node not in path:
				global int2
				int2 += 1
				print "if iter: %s" % int2
				
				newpath = self.go(graph, node, end, path)
				if newpath: return newpath
		return None
	
	'''
	def look(self):
		start = self.location
		if not graph.has_key(start):
			print "graph doesn't have key error"
			return None
		print "Nearby accessible locations: "
		for node in graph[start]:
			print node
	def go(self, end, path=[]):
	
		start = self.location
		path.append(start)

		if start == end:
			print "You are there."
			return path
		if not graph.has_key(start):
			print "graph doesn't have key error"
			return None
		for node in graph[start]:
			print "Debug: %s" % node
			if node in end:
				print "Going to %s" % node
				self.location = node
				break
p = Player()