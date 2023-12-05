"""
event modules
"""

from modules.exploration import map
from modules.exploration import movement
from modules.battle import enemy, battle
from modules.character import equipment


def open_the_door(character_dictionary, current_map):
    is_open = False
    while True:
        is_open = input(f"Do you want to open the door? (Y/N): ")
        if is_open.capitalize() == "Y":
            print(f"Yor are leaving this area...")
            map_list = map.maps()
            current_map = map.create_map(character_dictionary, map_list)
            movement.start_from_door(character_dictionary, current_map)
            return current_map
        elif is_open.capitalize() == "N":
            print(f"Maybe there is still something surprise here?")
            return current_map
        else:
            print(f"Please enter Y/N: ")


def encounter_an_enemy(character_dictionary, current_map):
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy.select_enemy(character_dictionary, enemy_dictionary)
    user_input = enemy.ask_user(enemy_appeared)
    is_enemy_killed = enemy.battle_talk_escape(
        character_dictionary, user_input, enemy_appeared)
    if is_enemy_killed:
        current_map[(character_dictionary["X-coordinate"],
                     character_dictionary["Y-coordinate"])] = "Empty"


def encounter_oberon(character_dictionary, current_map):
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy_dictionary["Miniboss"][2]
    user_input = enemy.ask_user(enemy_appeared)
    is_enemy_killed = enemy.battle_talk_escape(
        character_dictionary, user_input, enemy_appeared)
    if is_enemy_killed:
        current_map[(character_dictionary["X-coordinate"],
                     character_dictionary["Y-coordinate"])] = "Empty"
        

def encounter_cerberus(character_dictionary, current_map):
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy_dictionary["Miniboss"][1]
    user_input = enemy.ask_user(enemy_appeared)
    is_enemy_killed = enemy.battle_talk_escape(
        character_dictionary, user_input, enemy_appeared)
    if is_enemy_killed:
        current_map[(character_dictionary["X-coordinate"],
                     character_dictionary["Y-coordinate"])] = "Empty"

def encounter_dracula(character_dictionary, current_map):
    enemy_dictionary = enemy.enemy()
    enemy_appeared = enemy_dictionary["Miniboss"][3]
    user_input = enemy.ask_user(enemy_appeared)
    is_enemy_killed = enemy.battle_talk_escape(
        character_dictionary, user_input, enemy_appeared)
    if is_enemy_killed:
        current_map[(character_dictionary["X-coordinate"],
                     character_dictionary["Y-coordinate"])] = "Empty"
    
def find_a_chest(character_dictionary, current_map):
    get_equipment = equipment.get_equipment(character_dictionary)
    current_map[(character_dictionary["X-coordinate"],
                 character_dictionary["Y-coordinate"])] = "Empty"
    while True:
        if character_dictionary["Equipment"]:
            print(
                f"Your current equipment is: {character_dictionary['Equipment'][0]} {character_dictionary['Equipment'][1:]}")
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
    print("Take a sip of water, for rest is meant to pave the way for a longer journey ahead.")
    print("You get heal, HP +5")
    character_dictionary["Character_status"]["HP"] += 5
    current_map[(character_dictionary["X-coordinate"],
                 character_dictionary["Y-coordinate"])] = "Empty"
