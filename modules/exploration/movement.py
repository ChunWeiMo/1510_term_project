"""
Movement module.
"""
from modules.exploration import map, event
import random


def start_from_door(character_dictionary: dict, current_map: dict):
    """
    Put character starting at a random door.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: put character starting at a random door
    """
    doors = list()
    for coordinate in current_map:
        if current_map[coordinate] == 'Door':
            doors.append(coordinate)
    door_rand = doors[random.randint(0, len(doors) - 1)]
    character_dictionary["X-coordinate"] = door_rand[0]
    character_dictionary["Y-coordinate"] = door_rand[1]


def validate_move(character_dictionary: dict, direction: str, current_map: dict) -> bool:
    """
    Determine where the player is on the board and whether they can travel in their desired direction.

    :param character_dictionary: a dictionary of character attributes
    :param direction: a string
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :precondition: direction must be N, E, S, W
    :postcondition: determine whether they can travel in their desired direction
    :return: a boolean

    >>> character_dictionary_1 = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
    ...                                                 "LUK": 1, "VIS": 3},
    ...                            "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
    ...                            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
    ...                            "Equipment": 0, "Debuff": {"Burn": 0}}
    >>> current_map_1 = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
    >>> validate_move(character_dictionary_1, "S", current_map_1)
    True

    >>> character_dictionary_1 = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
    ...                                                 "LUK": 1, "VIS": 3},
    ...                            "Name": "describe", "X-coordinate": 0, "Y-coordinate": 0,
    ...                            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
    ...                            "Equipment": 0, "Debuff": {"Burn": 0}}
    >>> current_map_1 = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
    >>> validate_move(character_dictionary_1, "N", current_map_1)
    You are stopped by North wall
    <BLANKLINE>
    False
    """
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


def move_character(character_dictionary: dict, direction: str):
    """
    Move character forward a direction.

    :param character_dictionary: a dictionary of character attributes
    :param direction: a string
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: direction must be N, E, S, W
    :postcondition: move character forward a direction

    >>> character_dictionary_1 = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
    ...                                                 "LUK": 1, "VIS": 3},
    ...                            "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
    ...                            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
    ...                            "Equipment": 0, "Debuff": {"Burn": 0}}
    >>> move_character(character_dictionary_1, "N")
    moving toward North...

    >>> character_dictionary_1 = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
    ...                                                 "LUK": 1, "VIS": 3},
    ...                            "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
    ...                            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
    ...                            "Equipment": 0, "Debuff": {"Burn": 0}}
    >>> move_character(character_dictionary_1, "S")
    moving toward South...
    """
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


def describe_current_location(character: dict, current_map: dict):
    """
    Print character current position.

    :param character: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: print character current position.

    >>> character_dictionary_1 = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
    ...                                                 "LUK": 1, "VIS": 3},
    ...                            "Name": "describe", "X-coordinate": 1, "Y-coordinate": 1,
    ...                            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
    ...                            "Equipment": 0, "Debuff": {"Burn": 0}}
    >>> current_map_1 = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
    >>> describe_current_location(character_dictionary_1, current_map_1)
    You are at X: 1, Y: 1.
    <BLANKLINE>

    >>> character_dictionary_1 = {"Character_status": {"Level": 1, "HP": 100, "STR": 11, "DEF": 1, "CHR": 1, "SPD": 1,
    ...                                                 "LUK": 1, "VIS": 3},
    ...                            "Name": "describe", "X-coordinate": 2, "Y-coordinate": 2,
    ...                            "EXP": 0, "Items": {"Gold": 0, "Potions": 0},
    ...                            "Equipment": 0, "Debuff": {"Burn": 0}}
    >>> current_map_1 = {(0, 0): 'Empty', (1, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Empty'}
    >>> describe_current_location(character_dictionary_1, current_map_1)
    You are at X: 2, Y: 2.
    <BLANKLINE>
    !!WARNING!!: Out of the board
    <BLANKLINE>
    """
    east_wall, south_wall = map.walls(current_map)
    print(
        f"You are at X: {character['X-coordinate']}, Y: {character['Y-coordinate']}.")
    print()
    if (character['X-coordinate'] > east_wall or character['X-coordinate'] < 0 or character['Y-coordinate'] >
            south_wall or character['Y-coordinate'] < 0):
        print("!!WARNING!!: Out of the board")
        print()


def check_for_event(character_dictionary: dict, current_map: dict) -> tuple:
    """
    Check event when character touch a map element icon.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
     items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: check event when character touch a map element icon.
    """
    achieved_goal = False
    if current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] != "Empty":
        print(f'You meet {current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])]}!')
        print()
    if current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Door":
        current_map = event.open_the_door(character_dictionary, current_map)
    elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Enemy":
        event.encounter_an_enemy(character_dictionary, current_map)
    elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Oberon":
        event.encounter_oberon(character_dictionary, current_map)
    elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Cerberus":
        event.encounter_cerberus(character_dictionary, current_map)
    elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Dracula":
        event.encounter_dracula(character_dictionary, current_map)
    elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Final Boss":
        achieved_goal = event.encounter_final_boss(character_dictionary, current_map)
    elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Chest":
        event.find_a_chest(character_dictionary, current_map)
    elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Merchant":
        event.encounter_merchant(character_dictionary, current_map)
    elif (current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] ==
          "Healing_fountain"):
        event.rest_at_fountain(character_dictionary, current_map)
    return current_map, achieved_goal
