from player import Player
from room   import Room

# Declare all the rooms

room = {
    'outside':  Room( "Outside Cave Entrance",
                      "North of you, the cave mouth beckons" ),

    'foyer':    Room( "Foyer",
                      ''.join(
                          ( "Dim light filters in from the south. Dusty passages\n"
                            "run north and east." )
                        ) ),

    'overlook': Room( "Grand Overlook",
                      ''.join(
                          ( "A steep cliff appears before you, falling into the\n",
                            "darkness. Ahead to the north, a light flickers in\n",
                            "the distance, but there is no way across the chasm." )
                        ) ),

    'narrow':   Room( "Narrow Passage",
                      ''.join(
                          ( "The narrow passage bends here from west to north.\n",
                            "The smell of gold permeates the air." )
                        ) ),

    'treasure': Room( "Treasure Chamber",
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player( 'Bob' )

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
    print( room[ current_room ].get_name()                       )
    print( '---------------------------------------------------' )
    print( 'Description:'                                        )
    print( room[ current_room ].get_desc()                       )
    print( '---------------------------------------------------' )

    print( 'game_over' )
    game_running = False
