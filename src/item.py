#########################################
# Imports
#########################################
from colorama import Style, Fore


#########################################
# Item Class/SubClasses
#########################################
class Item:
    def __init__( self, name, desc ):
        self.__name        = name
        self.__description = desc


    def get_name( self ):
        return self.__name
    

    def get_desc( self ):
        return self.__description


    def on_take( self ):
        print( f'{Style.BRIGHT}{Fore.YELLOW}"You pick up { self.__name }"{Style.RESET_ALL}')


    def on_drop( self ):
        print( f'{Style.BRIGHT}{Fore.YELLOW}"You drop { self.__name }"{Style.RESET_ALL}' )


# LightSource Item SubClass
class LightSource( Item ):
    def __init__( self, name, desc ):
        super().__init__( name, desc )
    

    def on_drop( self ):
        print( f'{Fore.YELLOW}* You have made the unwise choice of dropping your light source!"' )


# Lantern LightSource Subclass
class Lantern( LightSource ):
    def __init__( self, name, desc ):
        super().__init__( name, desc )

        self.__carried = False


    def on_take( self ):
        self.__carried = True
        print( f'{Style.BRIGHT}{Fore.YELLOW}"You pick up the lantern"')
        print( f'{Style.NORMAL}* A soft, warm glow emits from the lantern, easily\nilluminating the surrounding area' )


# Weapon SubClass
class Weapon( Item ):
    def __init__( self, name, desc, style, dmg=20, dur=70, rarity='common' ):
        super().__init__( name, desc )

        self.__style      = style
        self.__damage     = dmg
        self.__durability = dur
        self.__rarity     = rarity

        def get_style( self ):
            return self.__style

        
        def get_damage( self ):
            return self.__damage

        
        def get_durability( self ):
            return self.__durability


        def get_rarity( self ):
            return self.__rarity
#########################################EoF
