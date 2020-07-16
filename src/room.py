# Implement a class to hold room information. This should have name and
# description attributes.


#########################################
class Room:
    def __init__( self, name, common, desc ):
        self.__name        = name
        self.__common_name = common
        self.__description = desc
        self.__n_to        = 'invalid'
        self.__s_to        = 'invalid'
        self.__e_to        = 'invalid'
        self.__w_to        = 'invalid'
        self.__items       = []


    def get_name( self ):
        return self.__name


    def get_common_name( self ):
        return self.__common_name


    def get_desc( self ):
        return self.__description


    def set_n_to( self, room ):
        self.__n_to = room


    def get_n_to( self ):
        return self.__n_to


    def set_s_to( self, room ):
        self.__s_to = room


    def get_s_to( self ):
        return self.__s_to


    def set_e_to( self, room ):
        self.__e_to = room


    def get_e_to( self ):
        return self.__e_to


    def set_w_to( self, room ):
        self.__w_to = room

        
    def get_w_to( self ):
        return self.__w_to


    def add_item( self, item ):
        self.__items.append( item )


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
