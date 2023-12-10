"""
event modules
"""

from modules.exploration import map
from modules.exploration import movement
from modules.battle import enemy
from modules.character import equipment, items


def open_the_door(character_dictionary: dict, current_map: dict) -> dict:
    """
    Create a new map when character open the door.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: if player input Y, create a random map according character level from map list
    :postcondition: put character on a random door
    :postcondition: if player input N, stay
    :postcondition: keep looping until user enter Y or N
    :return: a dictionary
    """
    while True:
        is_open = input(f"Do you want to open the door? (Y/N): ")
        if is_open.capitalize() == "Y":
            print(f"You are leaving this area...")
            map_list = map.maps()
            current_map = map.create_map(character_dictionary, map_list)
            movement.start_from_door(character_dictionary, current_map)
            return current_map
        elif is_open.capitalize() == "N":
            print(f"Maybe there is still something to explore here?")
            return current_map
        else:
            print(f"Please enter Y/N: ")


def go_to_battle(character_dictionary, enemy_appeared, current_map):
    """
    Enter battle with an enemy.

    :param character_dictionary: a dictionary of character attributes
    :param enemy_appeared: a dictionary of enemy attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: enemy_appeared is a dictionary of Dracula's attributes
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: deletes the enemy that is killed on the map
    """
    is_enemy_killed = None
    while is_enemy_killed is None:
        user_input = enemy.ask_user(enemy_appeared)
        is_enemy_killed = enemy.battle_talk_escape(character_dictionary, user_input, enemy_appeared)
    if is_enemy_killed:
        current_map[(character_dictionary["X-coordinate"],
                     character_dictionary["Y-coordinate"])] = "Empty"


def encounter_an_enemy(character_dictionary: dict, current_map: dict):
    """
    Encounter a random enemy and decide battle, talk or run away.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: generate a random enemy according character level from enemy list
    :postcondition: if enemy is killed, change map element to Empty
    """
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy.select_enemy(character_dictionary, enemy_dictionary)
    go_to_battle(character_dictionary, enemy_appeared, current_map)


def encounter_oberon(character_dictionary: dict, current_map: dict):
    """
    Encounter Oberon and decide battle, talk or run away.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: encounter mini boss Oberon decide battle, talk or run away.
    :postcondition: if Oberon is killed, change map element to Empty
    """
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy_dictionary["Miniboss"][2]
    go_to_battle(character_dictionary, enemy_appeared, current_map)
        

def encounter_cerberus(character_dictionary: dict, current_map: dict):
    """
    Encounter Cerberus and decide battle, talk or run away.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: encounter mini boss Cerberus decide battle, talk or run away.
    :postcondition: if Cerberus is killed, change map element to Empty
    """
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy_dictionary["Miniboss"][1]
    go_to_battle(character_dictionary, enemy_appeared, current_map)


def encounter_dracula(character_dictionary: dict, current_map: dict):
    """
    Encounter Dracula and decide battle, talk or run away.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: encounter mini boss Dracula decide battle, talk or run away.
    :postcondition: if Dracula is killed, change map element to Empty
    """
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy_dictionary["Miniboss"][3]
    go_to_battle(character_dictionary, enemy_appeared, current_map)
        

def encounter_final_boss(character_dictionary: dict, current_map: dict) -> bool:
    """
    Encounter Final boss and battle

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: encounter mini boss Dracula decide battle, talk or run away.
    :postcondition: if Final boss is killed, assign true to achieve_goal
    :return: a boolean
    """
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy_dictionary["Final Boss"]
    achieved_goal = None
    while achieved_goal is None:
        user_input = enemy.ask_user(enemy_appeared)
        achieved_goal = enemy.battle_talk_escape(
            character_dictionary, user_input, enemy_appeared)
        if achieved_goal:
            current_map[(4, 5)] = "Empty"
            current_map[(5, 5)] = "Empty"
            current_map[(4, 4)] = "Empty"
            current_map[(5, 4)] = "Empty"
    return achieved_goal
        

def find_a_chest(character_dictionary: dict, current_map: dict):
    """
    Find a chest and decide whether to use it or not.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: change map element to Empty
    :postcondition: if character has no equipment, use it automatically
    :postcondition: if character has equipment, input Y to replace it with new equipment
    :postcondition: if character has equipment, input N keep original equipment
    """
    current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] = "Empty"
    is_use_equipment = ""
    get_equipment = equipment.get_equipment(character_dictionary)
    if character_dictionary["Equipment"] == 0:
        equipment.use_equipment(
                character_dictionary, character_dictionary['Equipment'], get_equipment)
    else:
        while True:
            if character_dictionary["Equipment"]:
                print(
                    f"Your current equipment is: {character_dictionary['Equipment'][0]} "
                    f"{character_dictionary['Equipment'][1:]}")
                is_use_equipment = input("Do you want to change it? (Y/N) ")
            if is_use_equipment.upper() == "Y":
                equipment.use_equipment(
                    character_dictionary, character_dictionary['Equipment'], get_equipment)
                print(f"Now you are using {get_equipment[0]}!")
                break
            elif is_use_equipment.upper() == "N":
                print("You prefer wielding familiar things right?")
                break


def rest_at_fountain(character_dictionary, current_map):
    """
    Heal 5 hp at healing fountain.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: heal 5 hp
    :postcondition: change map element to Empty

    >>> character_dictionary_1 = {"Character_status": {"Level": 2, "HP": 110, "STR": 30, "DEF": 10, "CHR": 1, "SPD": 1,
    ... "LUK": 1, "VIS": 3}, "Name": "heal", "X-coordinate": 2, "Y-coordinate": 7}
    >>> current_map_1 = {(2, 7): 'Healing_fountain'}
    >>> rest_at_fountain(character_dictionary_1, current_map_1)
    Take a sip of water, for rest is meant to pave the way for a longer journey ahead.
    You get heal, HP +5
    >>> character_dictionary_1
    {'Character_status': {'Level': 2, 'HP': 115, 'STR': 30, 'DEF': 10, 'CHR': 1, 'SPD': 1, 'LUK': 1, 'VIS': 3}, 'Name':\
 'heal', 'X-coordinate': 2, 'Y-coordinate': 7}
    """

    print("Take a sip of water, for rest is meant to pave the way for a longer journey ahead.")
    print("You get heal, HP +5")
    character_dictionary["Character_status"]["HP"] += 5
    current_map[(character_dictionary["X-coordinate"],
                 character_dictionary["Y-coordinate"])] = "Empty"


def encounter_merchant(character_dictionary: dict, current_map: dict):
    """
    Meet a merchant on the map.

    :param character_dictionary: a dictionary of character attributes
    :param current_map: a dictionary
    :precondition: attribute_points must be a positive integer
    :precondition: character_dictionary is a dictionary that includes character status, name, location, experience,
    items, equipment and debuffs
    :precondition: current_map must have element-coordinate as key-value pair
    :precondition: coordinate must be a tuple of integers
    :postcondition: trade with the merchant
    :postcondition: change map element to Empty
    """
    items.merchant(character_dictionary)
    current_map[(character_dictionary["X-coordinate"],
                 character_dictionary["Y-coordinate"])] = "Empty"
