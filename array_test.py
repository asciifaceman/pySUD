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
World = [('0,0', '0,1', '0,2'), 
	('1,0', '1,1', '1,2'), 
	('2,0', '2,1', '2,2')]
Desc = [('Start location', 'right of start', 'further right of start'),
	('middle left', 'true middle', 'middle right'),
	('top left', 'top middle', 'top right')]
	
start = [0, 0]
# start[0] = Y
# start[1] = X

print "You are currently at: %s" % Desc[start[0]][start[1]]
print "Available actions: N, S, E, W"
def Here():
	print "You are currently at: %s" % Desc[start[0]][start[1]]

# Logic movements, tried to build it to handle any world size.
# Currently does not support inaccessible rooms or anything, much more code later

#TODO: Give rooms attributes
#TODO: Determine room entry and exit vectors 

def Move(direction):
	direction = direction.lower()
	
	if direction == "n" or direction == "north":
		if (start[0] + 1) >= len(World[0][:]):
			print "Cannot move that direction, there is nowhere to go"
		else:
			print "moving north"
			start[0] += 1
	elif direction == "e" or direction == "east":
		if (start[1] + 1) >= len(World[1][:]):
			print "Cannot move that direction, there is nowhere to go"
		else:
			print "moving east"
			start[1] += 1	
	elif direction == "s" or direction == "south":
		if (start[0] - 1) <= -1:
			print "Cannot move that direction, there is nowhere to go"
		else:
			print "moving east"
			start[0] -= 1	
	elif direction == "w" or direction == "west":
		if (start[1] - 1) <= -1:
			print "Cannot move that direction, there is nowhere to go"
		else:
			print "moving east"
			start[1] -= 1	










