#
#
#
# pySOG.py

class Room:

    def __init__(self, id):
        self.description = ''#
        self.id = id
        self.connections = {}
        
    def addConnection( self, dir, room ):
        self.connections[dir] = room
        
    def printExits( self ):
        print 'There are', len( self.connections ), 'paths out:'
        for dir,room in self.connections.items():
            print 'To the', dir, ':', room.id
        
class Character(Room):
	def __init__(self):
		self.name = "Chas"
		self.loc = 'a' #initialize to spawn room
# end class Room

a = Room('A')
b = Room('B')
c = Room('C')
d = Room('D')
e = Room('E')

#b.addConnection( 'north', a )
b.addConnection( 'west', c )
b.addConnection( 'south', e )
b.addConnection( 'east', d )

a.addConnection( 'south', b )
a.description = '''This is where you spawn. 
Once you leave here, you will not be able to return.
IF you leave you must restart to create a new game.
To create a new game other shit you do.'''
c.addConnection( 'east', b )
b.description = '''You are on a narrow path between the solid rock 
wall between you andwhat  used to be your spawn point, 
and a larger path going opposite directions'''
e.addConnection( 'north', b )
d.addConnection( 'west', b )

#print "[%s]\n\n" % b.description
#b.printExits()
Player = Character()
