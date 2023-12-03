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
    character_stats = {"Level": 1, "HP": 80, "STR": 10,
                       "DEF": 7, "CHR": 3, "SPD": 5, "LUK": 9, "VIS": 3}
    character_name = "lionheartmo"
    character_1 = {"Character_status": character_stats,
                            "Name": character_name,
                            "X-coordinate": 0,
                            "Y-coordinate": 0,
                            "EXP": 0,
                            "Items": {"Gold": 0, "Potions": 0},
                            "Equipment": ["The lance of curses", ("STR", 6), ("HP", -30)],
                            "Debuff": {"Burn": 0}
                            }

    map_list = map.maps()
    current_map = map.create_map(character_1, map_list)
    movement.start_from_door(character_1, current_map)

    # ==================
    # test playing
    # ==================
    command = "not assign"
    while command.upper != "Q":
        print()
        vision.print_vision(character_1, current_map)
        movement.describe_current_location(character_1, current_map)
        
        print("Command list")
        print("Move a direction: N / E / S / W")
        print("Save or Load a play data: SAVE / LOAD")
        print("Show character stats: STATS")
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
                        f'You meet {current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])]}!')
                    print()
                if current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] == "Door":
                    current_map = event.open_the_door(character_1, current_map)
                elif current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] == "Enemy":
                    event.encounter_an_enemy(character_1, current_map)
                elif current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] == "Chest":
                    event.find_a_chest(character_1, current_map)
                elif current_map[(character_1["X-coordinate"], character_1["Y-coordinate"])] == "Healing_fountain":
                    event.rest_at_fountain(character_1, current_map)
        elif command.upper() == "STATS":
            print(character_1["Character_status"])
            print()
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
