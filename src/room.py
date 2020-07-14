# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__( self, name, desc ):
        self.name        = name
        self.description = desc
        self.n_to        = 'invalid'
        self.s_to        = 'invalid'
        self.e_to        = 'invalid'
        self.w_to        = 'invalid'

    def get_desc( self ):
        return self.description
