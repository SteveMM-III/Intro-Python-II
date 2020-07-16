#########################################
# Imports
#########################################
from player   import Player
from room     import Room
from item     import Item, Lantern, Weapon
from colorama import init, Fore, Back, Style


#########################################
# Setup
#########################################
# Colorama init
init()


# Declare all the rooms
room = {
    'outside':  Room( "outside",
                      "Outside Cave Entrance",
                      "North of you, the cave mouth beckons" ),

    'foyer':    Room( "foyer",
                      "Foyer",
                      ''.join(
                          ( "Dim light filters in from the south. Dusty passages\n"
                            "run north and east." ) )
                ),

    'overlook': Room( "overlook",
                      "Grand Overlook",
                      ''.join(
                          ( "A steep cliff appears before you, falling into the\n",
                            "darkness. Ahead to the north, a light flickers in\n",
                            "the distance, but there is no way across the chasm." ) )
                ),

    'narrow':   Room( "narrow",
                      "Narrow Passage",
                      ''.join(
                          ( "The narrow passage bends here from west to north.\n",
                            "The smell of gold permeates the air." ) )
                ),

    'treasure': Room( "treasure",
                      "Treasure Chamber",
                      ''.join(
                          ( "You've found the long-lost treasure chamber! Sadly,\n"
                            "it has already been completely emptied by earlier\n"
                            "adventurers. The only exit is to the south." ) )
                ),
}


# Link rooms together
room[ 'outside'  ].set_n_to( room[ 'foyer'    ] )
room[ 'foyer'    ].set_s_to( room[ 'outside'  ] )
room[ 'foyer'    ].set_n_to( room[ 'overlook' ] )
room[ 'foyer'    ].set_e_to( room[ 'narrow'   ] )
room[ 'overlook' ].set_s_to( room[ 'foyer'    ] )
room[ 'narrow'   ].set_w_to( room[ 'foyer'    ] )
room[ 'narrow'   ].set_n_to( room[ 'treasure' ] )
room[ 'treasure' ].set_s_to( room[ 'narrow'   ] )


# Create items
lamp  = Lantern( 'lantern', 'A magical lantern that glows brightly when held' )
sword = Weapon( 'sword', 'A normal sword with no special attributes or abilities', 'sword' )


# Add items to rooms
room[ 'foyer'    ].add_item( lamp  )
room[ 'overlook' ].add_item( sword )


#########################################
# Functions
#########################################
def invalid_option():
    print( f'{Fore.WHITE}[ {Fore.RED}Invalid option{Fore.WHITE} ]' )


#######
def blocked():
    print( f'{Fore.RED}Direction blocked! Please try again.{Fore.WHITE}' )


#######
def moving_on():
    print( f'{Fore.WHITE}[ {Fore.MAGENTA}moving on...   {Style.RESET_ALL}]' )


#######
def process_player_action( player, action ):
    if action in [ 'n', 's', 'e', 'w', 'i', 'l' ]:
        current_room = player.get_room()

        if   action == 'n':
            try:
                player.move_to( room[ current_room ].get_n_to().get_name() )
                print( ''.join( ( f'{Style.BRIGHT}{Fore.YELLOW}',
                                  f'"You move to the North"{Fore.WHITE}' ) )
                )
            except:
                blocked()
        
        elif action == 's':
            try:
                player.move_to( room[ current_room ].get_s_to().get_name() )
                print( ''.join( ( f'{Style.BRIGHT}{Fore.YELLOW}',
                                  f'"You move to the South"{Fore.WHITE}' ) )
                )
            except:
                blocked()
        
        elif action == 'e':
            try:
                player.move_to( room[ current_room ].get_e_to().get_name() )
                print( ''.join( ( f'{Style.BRIGHT}{Fore.YELLOW}',
                                  f'"You move to the East"{Fore.WHITE}' ) )
                )
            except:
                blocked()

        elif action == 'w':
            try:
                player.move_to( room[ current_room ].get_w_to().get_name() )
                print( ''.join( ( f'{Style.BRIGHT}{Fore.YELLOW}',
                                  f'"You move to the West"{Fore.WHITE}' ) )
                )
            except:
                blocked()
        
        elif action == 'l':
            current_room = room[ player.get_room() ]
            items        = current_room.get_items()

            print( f'{Style.BRIGHT}{Fore.YELLOW}"You search the area and find the following items:"{Style.NORMAL}')

            for i, itm in enumerate( items ):
                print( f'{Fore.WHITE}- {Fore.CYAN}{ itm.get_name().capitalize() }' )
            
            option = input( ''.join( ( f'{Style.RESET_ALL}You may {Fore.WHITE}',
                                       f'[ {Fore.CYAN}take item_name{Fore.WHITE} ] or ',
                                       f'[ {Fore.WHITE}({Fore.CYAN}c{Fore.WHITE})ontinue ] \n> {Fore.GREEN}' ) )
            )
            option = option.split()

            if len( option ) > 0:
                if option[ 0 ] == 'c':
                    moving_on()

                elif len(option) > 1 and option[ 0 ] == 'take':
                    found = False

                    for i, itm in enumerate( items ):
                        if itm.get_name() == option[ 1 ].lower():
                            found = True
                            itm.on_take()
                            current_room.remove_item( option[ 1 ] )
                            player.add_item( itm )
                            break
                    
                    if not found:
                        print( f'{Fore.WHITE}[ {Fore.MAGENTA}nothing taken {Style.RESET_ALL}]' )
                else:
                    invalid_option()
                    moving_on()

            else:
                moving_on()

        elif action == 'i':
            inv          = player.get_items()
            current_room = room[ player.get_room() ]

            print( f'{Fore.WHITE}[ {Fore.MAGENTA}You have the following items {Style.RESET_ALL}]' )

            for i, itm in enumerate( inv ):
                print( f'{Fore.WHITE}- {Fore.CYAN}{ itm.get_name().capitalize() }' )

            option = input( ''.join( ( f'{Style.RESET_ALL}You may {Fore.WHITE}',
                                    f'[ {Fore.CYAN}drop item_name{Fore.WHITE} ] or ',
                                    f'[ {Fore.WHITE}({Fore.CYAN}c{Fore.WHITE})ontinue ] \n> {Fore.GREEN}' ) )
            )
            option = option.split()

            if len( option ) > 0:
                if option[ 0 ] == 'c':
                    moving_on()

                elif len(option) > 1 and option[ 0 ] == 'drop':
                    found = False

                    for i, itm in enumerate( inv ):
                        if itm.get_name() == option[ 1 ].lower():
                            found = True
                            itm.on_drop()
                            current_room.add_item( itm )
                            player.remove_item( option[ 1 ] )
                            break

                    if not found:
                        print( f'{Fore.WHITE}[ {Fore.MAGENTA}nothing dropped {Style.RESET_ALL}]' )
                
                else:
                    invalid_option()
                    moving_on()
            else:
                moving_on()


#######
def get_player_action( player ):
    print( ''.join( ( f'[ ({Fore.CYAN}m{Fore.WHITE})ove, ',
                      f'({Fore.CYAN}i{Fore.WHITE})nventory, ',
                      f'({Fore.CYAN}l{Fore.WHITE})ook, or ',
                      f'({Fore.CYAN}q{Fore.WHITE})uit ]' ) )
    )

    action = input( f'What would you like to do? \n> {Fore.GREEN}' )
    action = action.lower()

    if   action == 'm':
        print( ''.join( ( f'{Fore.WHITE}[ ({Fore.CYAN}n{Fore.WHITE})orth, ',
                          f'({Fore.CYAN}s{Fore.WHITE})outh, ',
                          f'({Fore.CYAN}e{Fore.WHITE})ast, or ',
                          f'({Fore.CYAN}w{Fore.WHITE})est ]' ) )
        )

        direction = input( f'> {Fore.GREEN}' )
        direction = direction.lower()

        if direction not in [ 'n', 's', 'e', 'w' ]:
            invalid_option()
            return True
        else:
            process_player_action( player, direction )
            return True

    elif action == 'i':
        inv = player.get_items()

        if len( inv ) > 0:
            process_player_action( player, 'i' )

        else:
            print( f'{Fore.WHITE}[ {Fore.MAGENTA}Your inventory is empty {Style.RESET_ALL}]' )
        
        return True

    elif action == 'l':
        current_room = room[ player.get_room() ]
        items        = current_room.get_items()

        if len( items ) > 0:
            process_player_action( player, 'l' )

        else:
            print( f'{Style.BRIGHT}{Fore.YELLOW}"You search the area and find nothing of interest."')

        return True

    elif action == 'q':
        print( ''.join( ( f'{Fore.WHITE}Thanks for playing ',
                          f'{Fore.GREEN}{ player.get_name() }!' ) )
        )
        return False

    else:
        invalid_option()
        return True


#########################################
# Main
#########################################
# Make a new player object that is currently in the 'outside' room.
print( f'{Fore.WHITE}Welcome to Adventure Game!' )

player_name = input( f'Enter a name for your character: \n> {Fore.GREEN}' )

player = Player( player_name )

# Loop conditional
game_running = True

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while game_running:
    current_room = player.get_room()
    
    print( ''.join( ( f'{Style.NORMAL}{Fore.WHITE}[ Current Location: ',
                      f'{Fore.CYAN}{ room[ current_room ].get_common_name() }',
                      f'{Fore.WHITE} ]' ) )
    )
    print( f'{Fore.YELLOW}* { room[ current_room ].get_desc() }{Fore.WHITE}' )

    game_running = get_player_action( player )
#########################################EoF
