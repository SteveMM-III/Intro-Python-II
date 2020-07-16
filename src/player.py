# Write a class to hold player information, e.g. what room they are in
# currently.


#########################################
class Player:
    def __init__( self, name, room="outside" ):
        self.__name         = name
        self.__current_room = room
        self.__items        = []
        self.__weapon       = 'none'


    def get_name( self ):
        return self.__name


    def move_to( self, room ):
        self.__current_room = room


    def get_room( self ):
        return self.__current_room


    def add_item( self, item ):
        self.__items.append( item )
        if item.get_name() == 'sword':
            self.__weapon = item


    def remove_item( self, name ):
        if len( self.__items ) > 0:
            index = 'null'

            for i, itm in enumerate( self.__items ):
                if itm.get_name() == name:
                    index = i
                    break

            try:
                del( self.__items[ index ] )
                return True
            except:
                return False
        else:
            return False


    def get_items( self ):
        return self.__items
#########################################EoF
