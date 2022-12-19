# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:25:14 2022

@author: puniaa
"""
'''
This program is a simulation for pokemon

'''

#moving the pokemon based on direction

def move_pokemon(org_location, direction, steps):
    row,col = org_location
    if row > 150: 
        row = 150
    elif col >150:
        col = 150
    elif col < 0:
         col = 0
    elif row < 0:
        row = 0
    if direction.lower() == 'n':
        ntuple = row - steps,col
    elif direction.lower() == "e":
        ntuple = row, col+steps
    elif direction.lower() == "s": 
        ntuple = row, col -steps
    elif direction.lower() == 'w':
        ntuple = row + steps, col
    else: 
        ntuple = row, col
    return ntuple

turns = input("How many turns? => ")
turns = int(turns)
print(turns)
pokemon_name = input("What is the name of your pikachu? => ").strip()
print(pokemon_name)
oft = input("How often do we see a Pokemom (turns)? => ")
oft = int(oft)
print(oft)

start_location = (75,75)
new_row, new_col = start_location

r_list = []
turn_counter=0 
print()
print("Starting simulation, turn 0 {} at (75,75)".format(pokemon_name))




while turn_counter < turns:
    direction = input("What direction does {} walk? => ".format(pokemon_name)).strip("\r")
    print(direction)
    new_row, new_col = move_pokemon((start_location), direction, 5)
    start_location = (new_row, new_col)
    turn_counter +=1 
    if turn_counter % oft == 0: 
        print("Turn {0:}, {1:} at {2:}".format(turn_counter, pokemon_name, start_location))
        meet_pokemon = str(input("What type of Pokeman do you meet (W)ater, (G)round => ")).strip("\r")
        print(meet_pokemon)
        if meet_pokemon.lower() == 'g': 
            new_row, new_col = move_pokemon((start_location), direction, -10)
            print("{0:} runs away from {1:}".format(pokemon_name,(new_row,new_col)))
            r_list.append("Lose")
        if meet_pokemon.lower() == 'w': 
            new_row, new_col = move_pokemon((start_location), direction,1)
            print(start_location)
            print("{} wins and moves to {}".format(pokemon_name,(new_row,new_col)))
            r_list.append("win")
        else: 
            r_list.append("No Pokemon")
    start_location = (new_row, new_col)
start_location = (new_row, new_col)
        
print("{0:} ends up at {1:}, Record: {2:}".format(pokemon_name, start_location, r_list))

    