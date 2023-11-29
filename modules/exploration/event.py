"""
event modules
"""

from modules.exploration import map
from modules.exploration import movement

def open_the_door(character_dictionary):
    is_open = False
    while True:
        is_open = input(f"Do you want to open the door? (Y/N): ")
        if is_open.capitalize() == "Y":
            print(f"Yor are leaving this area...")        
            map_list = map.map_list()
            current_map = map.create_map(character_dictionary, map_list)
            movement.start_from_door(character_dictionary, current_map)
            break
        elif is_open.capitalize() == "N":
            print(f"Maybe there is still something surprise here?")
            break
        else:
            print(f"Please enter Y/N: ")
            