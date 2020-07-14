# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__( self, name, room="outside" ):
        self.name         = name
        self.current_room = room

    def move_to( self, room ):
        self.current_room = room

    def get_room( self ):
        return self.current_room
