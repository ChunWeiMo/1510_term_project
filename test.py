import random
import json
from modules.exploration import map
from modules.exploration import vision
from modules.exploration import movement
from modules.exploration import event
from modules.battle import enemy
from modules.menu import saveload


def main():
    # character_1 = character.make_character()
    # print(character_1)
    character_1 = {'Character_status': {'Level': 1, 'HP': 100, 'STR': 11, 'DEF': 1, 'CHR': 1, 'SPD': 1, 'LUK': 1},
                   'X-coordinate': 5, 'Y-coordinate': 5, 'EXP': 0, 'Items': {'Gold': 0, 'Potions': 0}, 'vision_range': 3}

    map_list = map.map_list()
    current_map = map.create_map(character_1, map_list)
    movement.start_from_door(character_1, current_map)

    # ==================
    # test playing
    # ==================
    command = "not assign"
    while command.upper != "Q":
        vision.print_vision(character_1, current_map)
        print()
        print(character_1)
        movement.describe_current_location(character_1, current_map)
        
        print("Command list")
        print("Move a direction: N / E / S / W")
        print("Save or Load a play data: SAVE / LOAD")
        print("Quit game: Q")
        command = input("Enter a command: ")
        # print(f"command is {command}")
        print()
        if command.upper() == 'N' or command.upper() == 'E' or command.upper() == 'S' or command.upper() == 'W':
            direction = command.upper()
            can_move = movement.validate_move(
                character_1, direction, current_map)
            if can_move:
                movement.move_character(character_1, direction)
                if current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] != "Empty":
                    print(
                        f'You meet {current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])]}')
                if current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] == "Door":
                    current_map = event.open_the_door(character_1, current_map)
                elif current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] == "Enemy":
                    event.encounter_an_enemy(character_1, current_map)
        elif command.upper() == 'Q':
            print("\nThank you for playing.")
            print("Close the game.")
            break
        elif command.upper() == 'SAVE':
            saveload.savedata(character_1, current_map)
        elif command.upper() == "LOAD":
            character_1, current_map = saveload.loaddata(character_1, current_map)
        else:
            print("\nInvalid command.")
            print("Please enter a command again.")


if __name__ == "__main__":
    main()
