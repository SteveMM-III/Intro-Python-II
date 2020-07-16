from colorama import Style, Fore

class Item:
    def __init__( self, name, desc ):
        self.name        = name
        self.description = desc

    def get_name( self ):
        return self.name
    
    def get_desc( self ):
        return self.description

    def on_take( self ):
        print( f'{Style.BRIGHT}{Fore.YELLOW}"You pick up { self.name }"{Style.RESET_ALL}')

    def on_drop( self ):
        print( f'{Style.BRIGHT}{Fore.YELLOW}"You drop { self.name }"{Style.RESET_ALL}' )

class LightSource( Item ):
    def __init__( self, name, desc ):
        super().__init__( name, desc )
    
    def on_drop( self ):
        print( f'{Fore.YELLOW}* You have made the unwise choice of dropping your light source!"' )

class Lantern( LightSource ):
    def __init__( self, name, desc ):
        super().__init__( name, desc )

        self.carried = False

    def on_take( self ):
        self.carried = True
        print( f'{Style.BRIGHT}{Fore.YELLOW}"You pick up the lantern"')
        print( f'{Style.NORMAL}* A soft, warm glow emits from the lantern, easily\nilluminating the surrounding area' )

class Weapon( Item ):
    def __init__( self, name, desc, style, dmg=20, dur=70, rarity='common' ):
        super().__init__( name, desc )

        self.style      = style
        self.damage     = dmg
        self.durability = dur
        self.rarity     = rarity
