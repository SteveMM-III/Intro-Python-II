# Implement a class to hold room information. This should have name and
# description attributes.


#########################################
class Room:
    def __init__( self, name, common, desc ):
        self.name        = name
        self.common_name = common
        self.description = desc
        self.n_to        = 'invalid'
        self.s_to        = 'invalid'
        self.e_to        = 'invalid'
        self.w_to        = 'invalid'
        self.items       = []


    def get_name( self ):
        return self.name


    def get_common_name( self ):
        return self.common_name


    def get_desc( self ):
        return self.description


    def get_n_to( self ):
        return self.n_to


    def get_s_to( self ):
        return self.s_to


    def get_e_to( self ):
        return self.e_to


    def get_w_to( self ):
        return self.w_to


    def add_item( self, item ):
        self.items.append( item )


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
