"""
Movement module.
"""
from modules.exploration import map
import random


def start_from_door(character_dictionary, current_map):
    doors = list()
    for coordinate in current_map:
        if current_map[coordinate]=='Door':
            doors.append(coordinate)
    door_rand = doors[random.randint(0, len(doors)-1)]
    character_dictionary["X-coordinate"] = door_rand[0]
    character_dictionary["Y-coordinate"] = door_rand[1]


def validate_move(character_dictionary, direction, current_map):
    north_wall, west_all = 0, 0
    south_wall, east_wall = map.walls(current_map)
    can_move = True
    if character_dictionary["Y-coordinate"] <= north_wall and direction == "N":
        can_move = False
        print("You are stopped by North wall\n")
    if character_dictionary["X-coordinate"] >= east_wall and direction == "E":
        can_move = False
        print("You are stopped by East wall\n")
    if character_dictionary["Y-coordinate"] >= south_wall and direction == "S":
        can_move = False
        print("You are stopped by South wall\n")
    if character_dictionary["X-coordinate"] <= west_all and direction == "W":
        can_move = False
        print("You are stopped by West wall\n")
    return can_move


def move_character(character_dictionary, direction):
    if direction == "N":
        character_dictionary["Y-coordinate"] -= 1
        print("moving toward North...")
    if direction == "E":
        character_dictionary["X-coordinate"] += 1
        print("moving toward East...")
    if direction == "S":
        character_dictionary["Y-coordinate"] += 1
        print("moving toward South...")
    if direction == "W":
        character_dictionary["X-coordinate"] -= 1
        print("moving toward West...")


def describe_current_location(character, current_map):
    east_wall, south_wall = map.walls(current_map)
    print(
        f"You are at X: {character['X-coordinate']}, Y: {character['Y-coordinate']}.")
    print()
    if character['X-coordinate'] > east_wall or character['X-coordinate'] < 0 or character['Y-coordinate'] > south_wall or character['Y-coordinate'] < 0:
        print("!!WARNING!!: Out of the board")
        print()
