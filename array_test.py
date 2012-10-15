#
'''
Array test in python
'''


'''
how I want it:
 
 -------------------
 - 2,0 - 2,1 - 2,2 -
 -------------------
 - 1,0 - 1,1 - 1,2 -
 -------------------
 - 0,0 - 0,1 - 0,2 -
 -------------------
 world[0][0] = 0,0
 world[0][1] = 0,1
 world[0][2] = 0,2
 world[2][0] = 2,0
'''
class Character(object):

	def __init__(self, name):
		self.name = name
		self.loc = ''
		self.inv = {} #'potion': 4, 'sword': 1

class World(object):
	def __init__(self, name):
		self.locName = name
		self.location = [('0,0', '0,1', '0,2'), 
			('1,0', '1,1', '1,2'), 
			('2,0', '2,1', '2,2')]
		self.desc = [('Start location', 'right of start', 'further right of start'),
			('middle left', 'true middle', 'middle right'),
			('top left', 'top middle', 'top right')]
	def Here(self):
		print "You are currently at: %s" % self.desc[start[0]][start[1]]
		print "Available actions: N, S, E, W"
		print
	def WorldInfo(self):
		print "This is the land named %s." % self.locName

	def Move(self, direction):
		vector = direction.lower()
		
		if vector == "n" or vector == "north":
			if (start[0] + 1) >= len(self.location[0][:]):
				print "Cannot go any further that direction."
			else:
				print "Moving north..."
				start[0] += 1
				self.Here()
		elif vector == "s" or vector == "south":
			if (start[0] - 1) <= -1:
				print "Cannot go any further that direction."
			else:
				print "Moving south..."
				start[0] -= 1
				self.Here()
		elif vector == "e" or vector == "east":
			if (start[1] + 1) >= len(self.location[1][:]):
				print "Cannot go any further that direction."
			else:
				print "Moving east..."
				start[1] += 1
				self.Here()
		elif vector == "w" or vector == "west":
			if (start[1] -1) <= -1:
				print "Cannot go any further that direction."
			else:
				print "Moving west..."
				start[1] -= 1
				self.Here()

#

'''
room class handling:
exits = [1, 0, 0, 1] #[N, S, E, W]
'''
#TODO: Give rooms attributes
#TODO: Determine room entry and exit vectors 

#

# Initialization and grand beginnings!

level = World('Terra')
start = [0, 0]


# start[0][] = Y
# start[][0] = X





