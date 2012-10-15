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
a.description = "This is your spawn point"
c.addConnection( 'east', b )
e.addConnection( 'north', b )
d.addConnection( 'west', b )

print "[%s]" % a.description
b.printExits()
