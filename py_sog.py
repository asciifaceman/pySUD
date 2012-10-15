# pySOG.py
class Room:
    def __init__(self, id, name=''):
        self.description = ''
        self.id = id
        self.name = name
        self.connections = {}
        
    def addConnection( self, dir, room ):
        self.connections[dir] = room
        
    def printExits( self ):
        print 'From {0}, there are {1} paths out:'.format(self.id, len(self.connections))
        for dir,room in self.connections.items():
            print 'To the', dir, ':', room.id
class Character:
	def __init__(self):
		self.name = "chas"
		self.loc = 'A'
		
# end class Room
roomList = {}

roomList['A'] = Room('A', 'Birth Springs')
roomList['A'].description = 'Your spawn point'
roomList['B'] = Room('B', 'Narrow Path')
roomList['B'].description = 'Empty Path'

b = Room('B')
b.description = 'Large central cavern'

c = Room('C')
d = Room('D')
e = Room('E')

b.addConnection( 'west', c )
b.addConnection( 'south', e )
b.addConnection( 'east', d )

roomList['A'].addConnection( 'south', b )
roomList['B'].addConnection( 'west', c )
roomList['B'].addConnection( 'south', e )
roomList['B'].addConnection( 'east', d )
c.addConnection( 'east', b )
e.addConnection( 'north', b )
d.addConnection( 'west', b )

Player = Character()
print roomList[Player.loc].printExits()
#b.printExits()
