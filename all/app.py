# Imports
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float 
from sqlalchemy.orm import Session

# Function Definitions
def is_valid_pokename(engine, poke_name):
    # sqlalchemy query to check if the provided poke_name exists in pokemon table
    # need to keep type checking here or else it will fail 
    # if a number is passed into the function because .casefold() only works on str data types
    if type(poke_name) is str and poke_name.casefold() == 'bulbasaur':
        return True
    return False

def is_valid_pokeid(engine, poke_id):
    # sqlalchemy query to check if the provided poke_id exists in pokemon table
    if poke_id == '1':
        return True
    return False

def get_pokeid_from_pokename(engine, poke_name):
    # sqlalchemy query to get pokemon id from poke_name
    return 1

def get_pokename_from_pokeid(engine, poke_id):
    # sqlalchemy query to get pokemon name from poke_id
    return 'bulbasaur'

def get_movename_from_moveid(engine, move_id):
    # sqlalchemy query to get move related to move_id
    return move_name

def print_pokegame_from_pokeid(engine, poke_id):
    # sqlalchemy query to get list of poke_games related to poke_id
    print() 

def print_types_from_pokeid(engine, poke_id):
    # sqlalchemy query to get weak to/strong against for each type for poke_id
    print()

def print_fx_from_pokeid(engine, poke_id, short=True):
    # sqlalchemy query to print abiltiies and their corresponding short/long fx
    if (short):
        print()
    else: #long
        print()

def print_moves_from_pokeid(engine, poke_id):
    # sqlalchemy query to get moves
    print()

def print_move_from_moveid(engine, move_id, poke_name):
    # sqlalchemy query to print move detail
    move_name = get_movename_from_moveid(move_id)
    print(f'Here are the stats for {move_name} that {poke_name} can learn:')
    print(f'the stats')

# returns poke_id if choice is a looping selection
# otherwise, returns 0
def process_inputs(engine, user_input, poke_id, poke_name):
    # process games
    if input == '1':
        print(f'Here are all the games {poke_name} can be found in:')
        print_pokegame_from_pokeid(engine, poke_id)
        return poke_id
    # process types
    elif input == '2':
        print(f'Here are the type(s) {poke_name} is weak to and strong against:')
        print_types_from_pokeid(engine,poke_id)
        return poke_id
    # process abilities
    elif input == '3':
        print(f"Here are {poke_name}'s possibile abilities:")
        print_fx_from_pokeid(engine, poke_id)
        ability_yn = input('Would you like to know more detail? (Y/N)').casefold()
        if (ability_yn == 'Y'):
            print_fx_from_pokeid(engine, poke_id, short=False)
        return poke_id
    # process moves
    elif input == '4':
        # loop here
        print(f"Here are {poke_name}'s moves:")
        print_moves_from_pokeid(engine, poke_id)
        moves_yn = input('Would you like to learn more about a move? (Y/N)').casefold()
        if (moves_yn == 'Y'):
            move_id = input("Please specific a move (#): ")
            print_move_from_moveid(engine, move_id)
        return poke_id
    # look at different pokemon
    elif input == '5':
        return 0 # return 0 to turn is_valid_pokexxx calls to False because 0 is an invalid Poke ID
    # if validation gets here, user wants to stop
    else:
        query_yn = input('Would you like to print out your query? (Y/N)').casefold()
        # Fix
        path = 'myFirstPath'
        if (query_yn == 'Y'):
            print(f'Thank you for using our Pokemon Database! Your printout can be found in {path}')
        else:
            print('Thank you for using our Pokemon Database!')
        return -1

# Main Loop
engine = 'thing'
poke_id = 0
while (poke_id == 0):
    print("Hello! Please indicate what Pokemon you would like to look up (You may refer to pokemon.csv for a list of all Pokemon and their IDs).")
    poke_input = input("Pokemon Name or ID: ").casefold()
    poke_name = ''
    if (is_valid_pokename(engine, poke_input)):
        poke_name=poke_input
        poke_id=get_pokeid_from_pokename(engine, poke_name)
    elif (is_valid_pokeid(engine, poke_input)):
        poke_id = poke_input
        poke_name = get_pokename_from_pokeid(engine, poke_id)

    while (is_valid_pokename(engine, poke_input) or is_valid_pokeid(engine, poke_input)):
        print('Would you like to know more about this Pokemon?')
        print('1. Game')
        print('2. Type Strengths/Weaknesses')
        print('3. Abilities')
        print('4. Moves')
        print('5. Back to Pokemon selection')
        print('X. End session')
        user_input = input('Enter choice: ')
        poke_input = process_inputs(engine, user_input, poke_id, poke_name)

# Make sure to add pokemon outputs and radar chart (and other graphs????)
