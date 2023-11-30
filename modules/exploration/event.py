"""
event modules
"""

from modules.exploration import map
from modules.exploration import movement
from modules.battle import enemy

def open_the_door(character_dictionary, current_map):
    is_open = False
    while True:
        is_open = input(f"Do you want to open the door? (Y/N): ")
        if is_open.capitalize() == "Y":
            print(f"Yor are leaving this area...")        
            map_list = map.map_list()
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
