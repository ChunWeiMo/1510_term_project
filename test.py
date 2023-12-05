import random
import json
from modules.exploration import map
from modules.exploration import vision
from modules.exploration import movement
from modules.exploration import event
from modules.exploration import story_lines
from modules.battle import enemy
from modules.menu import saveload
from modules.character import character


def main():
    # character_dictionary = character.make_character()
    # print(character_dictionary)
    # character_stats = {"Level": 1, "HP": 80, "STR": 10,
    #                    "DEF": 7, "CHR": 3, "SPD": 5, "LUK": 9, "VIS": 3}
    # character_name = "lionheartmo"
    # character_dictionary = {"Character_status": character_stats,
    #                         "Name": character_name,
    #                         "X-coordinate": 0,
    #                         "Y-coordinate": 0,
    #                         "EXP": 0,
    #                         "Items": {"Gold": 0, "Potions": 0},
    #                         "Equipment": ["The lance of curses", ("STR", 6), ("HP", -30)],
    #                         "Debuff": {"Burn": 0}
    #                         }

    achieved_goal = False
    achieved_goal_talk = False
    print(story_lines.welcome)
    character_dictionary = character.make_character()
    main_story = story_lines.get_story(character_dictionary)
    print(main_story["intro"])
    
    while character_dictionary["Character_status"]["HP"] > 0 and not achieved_goal and command.upper != "Q":
        map_list = map.maps()
        current_map = map.create_map(character_dictionary, map_list)
        movement.start_from_door(character_dictionary, current_map)

        # ==================
        # start playing
        # ==================
        command = "not assign"
        print()
        vision.print_vision(character_dictionary, current_map)
        movement.describe_current_location(character_dictionary, current_map)
        
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
                character_dictionary, direction, current_map)
            if can_move:
                movement.move_character(character_dictionary, direction)
                if current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] != "Empty":
                    print(
                        f'You meet {current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])]}!')
                    print()
                if current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Door":
                    current_map = event.open_the_door(character_dictionary, current_map)
                elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Enemy":
                    event.encounter_an_enemy(character_dictionary, current_map)
                elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Miniboss":
                    # mini boss
                    pass
                elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Final Boss":
                    # final boss
                    pass
                elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Chest":
                    event.find_a_chest(character_dictionary, current_map)
                elif current_map[(character_dictionary["X-coordinate"], character_dictionary["Y-coordinate"])] == "Healing_fountain":
                    event.rest_at_fountain(character_dictionary, current_map)
        elif command.upper() == "STATS":
            print(character_dictionary["Character_status"])
            print()
        elif command.upper() == 'Q':
            print("\nThank you for playing.")
            print("Close the game.")
            break
        elif command.upper() == 'SAVE':
            saveload.savedata(character_dictionary, current_map)
        elif command.upper() == "LOAD":
            character_dictionary, current_map = saveload.loaddata(character_dictionary, current_map)
        else:
            print("\nInvalid command.")
            print("Please enter a command again.")
    if character_dictionary["Character_status"]["HP"] <= 0:
        print(main_story["death"])
    if achieved_goal:
        print(main_story["win"])
    if achieved_goal_talk:
        print(main_story["win_talk"])


if __name__ == "__main__":
    main()
