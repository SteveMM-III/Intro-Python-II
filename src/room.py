# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__( self, name, common_name, desc ):
        self.name        = name
        self.common_name = common_name
        self.description = desc
        self.n_to        = 'invalid'
        self.s_to        = 'invalid'
        self.e_to        = 'invalid'
        self.w_to        = 'invalid'

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
