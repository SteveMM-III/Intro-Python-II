#########################################
# Imports
from player import Player
from room   import Room


#########################################
# Setup

# Declare all the rooms
room = {
    'outside':  Room( "outside",
                      "Outside Cave Entrance",
                      "North of you, the cave mouth beckons" ),

    'foyer':    Room( "foyer",
                      "Foyer",
                      ''.join(
                          ( "Dim light filters in from the south. Dusty passages\n"
                            "run north and east." )
                        ) ),

    'overlook': Room( "overlook",
                      "Grand Overlook",
                      ''.join(
                          ( "A steep cliff appears before you, falling into the\n",
                            "darkness. Ahead to the north, a light flickers in\n",
                            "the distance, but there is no way across the chasm." )
                        ) ),

    'narrow':   Room( "narrow",
                      "Narrow Passage",
                      ''.join(
                          ( "The narrow passage bends here from west to north.\n",
                            "The smell of gold permeates the air." )
                        ) ),

    'treasure': Room( "treasure",
                      "Treasure Chamber",
                      ''.join(
                          ( "You've found the long-lost treasure chamber! Sadly,\n"
                            "it has already been completely emptied by earlier\n"
                            "adventurers. The only exit is to the south." )
                        ) ),
}


# Link rooms together
room[ 'outside'  ].n_to = room[ 'foyer'    ]
room[ 'foyer'    ].s_to = room[ 'outside'  ]
room[ 'foyer'    ].n_to = room[ 'overlook' ]
room[ 'foyer'    ].e_to = room[ 'narrow'   ]
room[ 'overlook' ].s_to = room[ 'foyer'    ]
room[ 'narrow'   ].w_to = room[ 'foyer'    ]
room[ 'narrow'   ].n_to = room[ 'treasure' ]
room[ 'treasure' ].s_to = room[ 'narrow'   ]


#########################################
# Functions
def invalid_option():
    print( 'Invalid option' )


#######
def blocked():
    print( 'Direction blocked! Please try again.' )


#######
def process_player_action( player, action ):
    if action in [ 'n', 's', 'e', 'w' ]:
        current_room = player.get_room()

        if action == 'n':
            try:
                player.move_to( room[ current_room ].get_n_to().get_name() )
            except:
                blocked()
        
        elif action == 's':
            try:
                player.move_to( room[ current_room ].get_s_to().get_name() )
            except:
                blocked()
        
        elif action == 'e':
            try:
                player.move_to( room[ current_room ].get_e_to().get_name() )
            except:
                blocked()

        elif action == 'w':
            try:
                player.move_to( room[ current_room ].get_w_to().get_name() )
            except:
                blocked()

    print( 'Action processed' ) # remove after actions worked out


#######
def get_player_action( player ):
    print( 'Actions:  (m)ove, (i)nteract, or (q)uit' )

    action = input( 'What would you like to do? ' )
    action = action.lower()

    print( '---------------------------------------------------' )

    if action == 'm':
        print( ''.join( ( 'You have chosen to move.\n',
                          'Valid directions are (n)orth, (s)outh, (e)ast, or (w)est' )
                 ) )

        direction = input( 'Which direction would you like to move? ' )
        direction = direction.lower()

        print( '---------------------------------------------------' )

        if direction not in [ 'n', 's', 'e', 'w' ]:
            invalid_option()
            return True
        else:
            process_player_action( player, direction )
            return True

    elif action == 'i':
        print( 'There are currently no objects to interact with' )
        return True

    elif action == 'q':
        print( f'Thanks for playing, { player.get_name() }!' )
        return False

    else:
        invalid_option()
        return True


#########################################
# Main
#########################################
# Make a new player object that is currently in the 'outside' room.
print( 'Welcome to Adventure Game!' )

player_name = input( 'Enter a name for your character: ' )

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
    
    print( '---------------------------------------------------' )
    print( 'Current room/location:'                              )
    print( room[ current_room ].get_common_name()                )
    print( '---------------------------------------------------' )
    print( 'Description:'                                        )
    print( room[ current_room ].get_desc()                       )
    print( '---------------------------------------------------' )
    game_running = get_player_action( player )
#########################################EoF
