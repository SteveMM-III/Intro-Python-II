# Write a class to hold player information, e.g. what room they are in
# currently.


#########################################
class Player:
    def __init__( self, name, room="outside" ):
        self.name         = name
        self.current_room = room
        self.items        = []
        self.weapon       = 'none'


    def get_name( self ):
        return self.name


    def move_to( self, room ):
        self.current_room = room


    def get_room( self ):
        return self.current_room


    def add_item( self, item ):
        self.items.append( item )
        if item.get_name() == 'sword':
            self.weapon = item


    def remove_item( self, name ):
        if len( self.items ) > 0:
            index = 'null'

            for i, itm in enumerate( self.items ):
                if itm.get_name() == name:
                    index = i
                    break

            try:
                del( self.items[ index ] )
                return True
            except:
                return False
        else:
            return False


    def get_items( self ):
        return self.items
#########################################EoF
