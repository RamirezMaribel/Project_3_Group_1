# Imports
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float 
from sqlalchemy.orm import Session

# Database setup 
database_url = "postgresql://postgres:postgres@localhost:5432/pokemon_db" 
engine = create_engine(database_url) 
Base = declarative_base() 
Session = session(bind=engine)
conn=engine.connect()

# Function Definitions
def is_valid_pokename(conn, poke_name):
    # sqlalchemy query to check if the provided poke_name exists in pokemon table
    query = text(f"select poke_name from pokemon where poke_name='{poke_name}'")
    data = conn.execute(query)
    return data.rowcount == 1
    
def is_valid_pokeid(conn, poke_id):
    # sqlalchemy query to check if the provided poke_id exists in pokemon table
    query = text(f"select poke_id from pokemon where poke_id='{poke_id}'")
    data = conn.execute(query)
    return data.rowcount == 1


def get_pokeid_from_pokename(conn, poke_name):
    # sqlalchemy query to get pokemon id from poke_name
    query = text(f"select poke_id from pokemon where poke_name='{poke_name}'")
    data = conn.execute(query)
    return data.first()[0]
  

def get_pokename_from_pokeid(conn, poke_id):
    # sqlalchemy query to get pokemon name from poke_id
    query = text(f"select poke_name from pokemon where poke_id='{poke_id}'")
    data = conn.execute(query)
    return data.first()[0]

def get_movename_from_moveid(conn, move_id):
    # sqlalchemy query to get move related to move_id
    query = text(f"select move_name from move where move_id='{move_id}'")
    data = conn.execute(query)
    return data.first()[0]
    

def print_pokegame_from_pokeid(conn, poke_id):
    # sqlalchemy query to get list of poke_games related to poke_id
    query = text(f"select game_name from game where game_id in (select game_id from pokegame where poke_id='{poke_id}')")
    data = conn.execute(query)
    for row in data:
        print(row[0])

def print_types_from_pokeid(conn, poke_id):
    # sqlalchemy query to get weak to/strong against for each type for poke_id
    types_query = text(f"(select type from pokemon where poke_id='{poke_id}' union select second_type from pokemon where poke_id='{poke_id}')")
    for type_row in conn.execute(types_query):
        query = text (f"select weak_to, strong_against from type where type_name = '{type_row[0]}'")
        data = conn.execute(query)
        for row in data:
            print(type_row[0] + " is")
            print("weak to: "+ row[0])
            print("strong against: "+ row[1])

def print_fx_from_pokeid(conn, poke_id, short=True):
    # sqlalchemy query to print abiltiies and their corresponding short/long fx
    query = text(f"select effect, short_effect from ability where ability_name in (select ability_name from pokeability where poke_id='{poke_id}')")
    data = conn.execute(query)
    for row in data:
        if (short): 
            print(row[1])
        else: #long
            print(row[0])

def print_moves_from_pokeid(conn, poke_id):
    # sqlalchemy query to get moves
    print()

def print_move_from_moveid(conn, move_id, poke_name):
    # sqlalchemy query to print move detail
    move_name = get_movename_from_moveid(move_id)
    print(f'Here are the stats for {move_name} that {poke_name} can learn:')
    print(f'the stats')

# returns poke_id if choice is a looping selection
# otherwise, returns 0
def process_inputs(conn, user_input, poke_id, poke_name):
    # process games
    if user_input == '1':
        print(f'Here are all the games {poke_name} can be found in:')
        print_pokegame_from_pokeid(conn, poke_id)
        return poke_id
    # process types
    elif user_input == '2':
        print(f'Here are the type(s) {poke_name} is weak to and strong against:')
        print_types_from_pokeid(conn,poke_id)
        return poke_id
    # process abilities
    elif user_input == '3':
        print(f"Here are {poke_name}'s possibile abilities:")
        print_fx_from_pokeid(conn, poke_id)
        ability_yn = input('Would you like to know more detail? (Y/N)').casefold()
        if (ability_yn == 'Y'):
            print_fx_from_pokeid(conn, poke_id, short=False)
        return poke_id
    # process moves
    elif user_input == '4':
        # loop here
        print(f"Here are {poke_name}'s moves:")
        print_moves_from_pokeid(conn, poke_id)
        moves_yn = input('Would you like to learn more about a move? (Y/N)').casefold()
        if (moves_yn == 'Y'):
            move_id = input("Please specific a move (#): ")
            print_move_from_moveid(conn, move_id)
        return poke_id
    # look at different pokemon
    elif user_input == '5':
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

poke_id = 0
while (poke_id == 0):
    print("Hello! Please indicate what Pokemon you would like to look up (You may refer to pokemon.csv for a list of all Pokemon and their IDs).")
    poke_input = input("Pokemon Name or ID: ").casefold()
    poke_name = ''
    if (is_valid_pokename(conn, poke_input)):
        poke_name=poke_input
        poke_id=get_pokeid_from_pokename(conn, poke_name)
    elif (is_valid_pokeid(conn, poke_input)):
        poke_id = poke_input
        poke_name = get_pokename_from_pokeid(conn, poke_id)

    while (is_valid_pokename(conn, poke_input) or is_valid_pokeid(conn, poke_input)):
        print('Would you like to know more about this Pokemon?')
        print('1. Game')
        print('2. Type Strengths/Weaknesses')
        print('3. Abilities')
        print('4. Moves')
        print('5. Back to Pokemon selection')
        print('X. End session')
        user_input = input('Enter choice: ')
        poke_input = process_inputs(conn, user_input, poke_id, poke_name)

# Make sure to add pokemon outputs and radar chart (and other graphs????)
